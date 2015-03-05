from sqlalchemy.ext.declarative import declarative_base


class ValidationError(Exception):
    pass


Base = declarative_base()
