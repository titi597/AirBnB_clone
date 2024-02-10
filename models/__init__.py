#!/usr/bin/python3
from models.engine.file_storage import FileStorage


class StorageManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = FileStorage()
            cls._instance.reload()
        return cls._instance

storage = StorageManager.get_instance()
