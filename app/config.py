import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    AZS = os.environ.get("AZURE_STORAGE_CONNECTIONSTRING") or "smstr"
    AZS_CONTAINER = os.environ.get("AZS_CONTAINER") or "alise"
