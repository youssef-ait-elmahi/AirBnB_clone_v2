#!/usr/bin/python3
""" Models package """
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
