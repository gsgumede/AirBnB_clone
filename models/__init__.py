#!/usr/bin/python3
"""Create a unique FliStorage application instance"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()