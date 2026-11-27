import os
from pathlib import Path
from sys import prefix

import boto3
from botocore.retries.adaptive import bucket
from dotenv import load_dotenv
from mutagen.mp3 import MP3

load_dotenv()


class S3:
    def __init__(self):
        self.bucket_name = os.getenv("S3_BUCKET_NAME")
        self.region = os.getenv("AWS_REGION")
        self.client = boto3.client("s3", region_name=self.region)

    def get_audio_duration(self, file_path: str) -> str:
        """Get the total time of mp3 file"""
        audio = MP3(file_path)
        total_seconds = int(audio.info.length)

        minutes, seconds = divmod(total_seconds, 60)

        return f"{minutes}:{seconds:02d}"

    def upload_mp3(self, session_id: str, file_path: str) -> str:
        """Upload one MP3 file to session's S3 prefix"""
        if not session_id or "/" in session_id or "\\" in session_id:
            raise ValueError("Invalid Session ID")

        path = Path(file_path)

        if not path.is_file():
            raise FileNotFoundError(path)

        if path.suffix.lower() != ".mp3":
            raise ValueError("Only mp3 files are allowed")

        object_key = f"not_saved/{session_id}/{path.name}"

        self.client.upload_file(
            str(path),
            self.bucket_name,
            object_key,
            ExtraArgs={"ContentType": "audio/mpeg"},
        )
        return object_key

    def get_playback_url(self, object_key: str, expires_in: int = 3600) -> str:
        """Generate a temp URL for a playing an S3 object."""

        if not 1 <= expires_in <= 604800:
            raise ValueError("Expires_In must be between 1 and 604800 seconds")

        return self.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": self.bucket_name, "Key": object_key},
            ExpiresIn=expires_in,
        )

    def delete_mp3(self, object_key: str) -> None:
        """Delete one s3 object"""
        self.client.delete_object(Bucket=self.bucket_name, Key=object_key)

    def move_session_to_saved(self, session_id: str) -> list[str]:
        """Move all objects for a sessions from not_saved/ to saved/"""
        if not session_id or "/" in session_id or "\\" in session_id:
            raise ValueError("Invalid session_id")

        src_prefix = f"not_saved/{session_id}"
        dst_prefix = f"saved/{session_id}"

        paginator = self.client.get_paginator("list_objects_v2")

        source_keys = []

        for page in paginator.paginate(
            bucket=self.bucket_name,
            prefix=src_prefix,
        ):
            for obj in page.get("Content", []):
                source_keys.append(obj["Key"])

        if not source_keys:
            return []
        moved_keys = []

        for src_key in source_keys:
            destination_key = dst_prefix + src_key[len(src_prefix) :]

            self.client.copy_object(
                bucket=self.bucket_name,
                key=destination_key,
                copysource={"Bucket": self.bucket_name, "Key": src_key},
            )

            moved_keys.append(destination_key)
            # Delete the orginals only after all copies succeed.
            if moved_keys:
                response = self.client.delete_objects(
                    Bucket=self.bucket_name,
                    Delete={
                        "Objects": [
                            {"Key": src_prefix + key[len(dst_prefix) :]}
                            for key in moved_keys
                        ],
                        "Quiet": True,
                    },
                )
            if response.get("Errors"):
                raise RuntimeError(
                    f"Some original S3 objects could not be deleted: {response['Errors']}"
                )
        return moved_keys


s3 = S3()
