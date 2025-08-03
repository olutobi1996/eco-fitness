from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaStorage(S3Boto3Storage):
    location = "media"  # all uploaded files go under "media/" in your bucket
    default_acl = "public-read"
    file_overwrite = False
