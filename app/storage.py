from .azureconn import BlobStorage
from time import time

blob_storage = BlobStorage()


def id_gen():
    # unique instance prefix generator
    i = 0
    while True:
        yield f"inst_pref_{int(time()*1000)}_{i}"
        i += 1


gn = id_gen()


def get(file_id):
    blob_bytes = blob_storage.download_file(file_id)
    return blob_bytes


def put(stream):
    file_id = blob_storage.upload_file(next(gn), stream)
    return file_id
