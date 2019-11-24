from app import app
from azure.storage.blob import BlobServiceClient
import azure.core.exceptions as az_exc
from werkzeug import exceptions


class BlobStorage:
    def __init__(self):
        self.connection_string = app.config.get("AZS")
        self.service = BlobServiceClient.from_connection_string(conn_str=self.connection_string)
        self._container_name = None
        self._container_client = None

    @property
    def container_name(self):
        if self._container_name:
            return self._container_name
        else:
            self._container_name = app.config.get("AZS_CONTAINER")
            return self._container_name

    @property
    def container_client(self):
        if self._container_client:
            return self._container_client
        else:
            try:
                self._container_client = self.service.create_container(self.container_name)
            except az_exc.ResourceExistsError:
                self._container_client = self.service.get_container_client(self.container_name)
            self._container_client = self._container_client
            return self._container_client

    def get_blob_client(self, blob_name):
        blob_client = self.service.get_blob_client(container=self.container_name, blob=blob_name)
        return blob_client

    def upload_file(self, name, stream):
        blob_client = self.get_blob_client(name)
        try:
            blob_client.upload_blob(stream)
        except az_exc.ResourceExistsError as e:
            print("DLOG: FAULT UPLOAD")
            raise exceptions.Conflict()
        return name

    def download_file(self, name):
        blob_client = self.get_blob_client(name)
        try:
            return blob_client.download_blob().readall()
        except Exception as e:  # dunno exception yet
            print("DLOG: FAULT DOWNLOAD")
            raise exceptions.NotFound(name)

    def list_all(self):
        bl = self.container_client.list_blobs()
        return [blob.name for blob in bl]

    def clear_all(self):
        cc = self.container_client
        cc.delete_container()
        return "All files gone"
