from pymongo.database import Database

def patched_bool(self):
    return True

Database.__bool__ = patched_bool