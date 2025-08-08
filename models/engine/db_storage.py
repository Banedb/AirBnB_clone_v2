#!/usr/bin/python3
"""db_storage module"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class manages database storage."""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{db}',
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        if cls:
            for obj in self.__session.query(cls):
                key = f"{obj.__class__.__name__}.{obj.id}"
                # obj.__dict__.pop('_sa_instance_state', None)
                new_dict[key] = obj
        else:
            for clss in [State, City, User, Amenity, Place, Review]:
                for obj in self.__session.query(clss):
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    # obj.__dict__.pop('_sa_instance_state', None)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Adds the object to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session if obj."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
