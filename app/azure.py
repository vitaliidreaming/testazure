from app import app
from azure.storage.blob import BlobServiceClient
connection_string = app.config.get('AZS')
service = BlobServiceClient.from_connection_string(conn_str=connection_string)