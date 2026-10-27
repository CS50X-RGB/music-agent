import os
from pathlib import Path
import boto3
from dotenv import load_dotenv

load_dotenv()

class S3:
    def __init__(self):
        self.bucket_name = os.getenv("S3_BUCKET_NAME")
        self.region = os.getenv("AWS_REGION")
        self.client = boto3.client('s3',region_name=self.region)
    
    def upload_mp3(self,session_id: str,file_path : str) -> str:
        """Upload one MP3 file to session's S3 prefix"""
        if not session_id or "/" in session_id or "\\" in session_id:
            raise ValueError("Invalid Session ID")
        
        path = Path(file_path)
        
        if not path.is_file():
            raise FileNotFoundError(path)
        
        
        if path.suffix.lower() != ".mp3":
            raise ValueError("Only mp3 files are allowed")
        
        object_key = f"not_saved/{session_id}/{path.name}"
        
        self.client.upload_file(str(path),self.bucket_name,object_key,ExtraArgs={
            "ContentType" : "audio/mpeg"
        })
        return object_key
    
    def get_playback_url(self,object_key : str,expires_in : int = 900) -> str:
        """Generate a temp URL for a playing an S3 object."""
        
        if not 1 <= expires_in <= 604800:
            raise ValueError("Expires_In must be between 1 and 604800 seconds")

        return self.client.generate_presigned_url("get_object",Params={
                "Bucket" : self.bucket_name,
                "Key"  : object_key
            },
            ExpiresIn=expires_in
        )
        
    def delete_mp3(self,object_key : str) -> None:
        """Delete one s3 object"""
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=object_key
        )
    
    def move_session_to_saved(self,session_id : str) -> list[str]:
        """Move all objects for a sessions from not_saved/ to saved/"""
        if not session_id or "/" in session_id or "\\" in session_id:
            raise ValueError("Invalid session_id")
        
        src_prefix = f"not_saved/{session_id}"
        dst_prefix = f"saved/{session_id}"
        
        response = self.client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=src_prefix,
        )
        
        objects = response.get("Contents",[])
        
        if not objects:
            return []
        
        # Copy first, then delete the orginals.
        moved_keys = []
        
        for obj in objects:
            src_key = obj["key"]
            
            if src_prefix == src_key:
                continue
            
            destination_key = (
                destination_key + src_key[len(src_prefix):]
            )
            
            self.client.copy_object(
                Bucket=self.bucket_name,
                Key=destination_key,
                CopySource={
                    "Bucket" : self.bucket_name,
                    "Key" : src_key,
                }
            )
            
            moved_keys.append(destination_key)
            
            # Delete the orginals only after all copies succeed.
            if moved_keys:
                self.client.delete_objects(
                    Bucket=self.bucket_name,
                    Delete={
                        "Objects" : [
                            {
                                "Key" : src_prefix + key[len(dst_prefix):]
                            }
                            for key in moved_keys
                        ],
                        "Quiet" : True
                    }
                )
            return moved_keys
        
        
s3 = S3()