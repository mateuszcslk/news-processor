from typing import List
import boto3
import constants
import os


class S3():
    def __init__(self, aws_access_key_id: str = constants.AWS_ACCESS_KEY_ID,
                 aws_secret_access_key: str = constants.AWS_SECRET_ACCESS_KEY,
                 bucket_name: str = constants.AWS_BUCKET_NAME):

        self.bucket_name = bucket_name
        self.s3_client = boto3.client(service_name='s3', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key)


    def upload(self, filepaths_to_upload: List[str]) -> None:
        for f in filepaths_to_upload:
            fname = os.path.split(f)[1]
            with open(f, "rb") as filecontent:
                self.s3_client.upload_fileobj(filecontent, self.bucket_name, fname)