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
    
    def upload_mp3(self,session_id: str,file_path : str,filename : str) -> str:
        return