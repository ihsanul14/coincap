from decouple import config
from sqlalchemy import create_engine


class Database:
    def sql_lite(self):
        engine = create_engine(config('SQLITE_URI'))
        return engine
