import headlines
import constants
import s3


def run():
    h = headlines.Headlines()
    files_to_push = h.list_files()

    s3_container = s3.S3()
    s3_container.upload(filepaths_to_upload=files_to_push)


if __name__ == "__main__":
    run()