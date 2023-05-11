#!/usr/bin/python3
""" Defining the base model class """
    """
        The class where other classes inherit from
    """
import models
import uuid import uuid4
from datetime import datetime


class BaseModel:
    """ The class that encapsulate other classes """
    def __init__(self, *args, **kwargs):
        """
            Initialization of the BaseClass
        """
        tfmt = %Y-%m-%dT%H:%M:%S.%f
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.striptime(v, tfmt)
                else:
                    self.__dict__[k] = v
		else:
			models.storage.new(self)
	
	def save(self):
        """
			Time creation or updating
		"""
        self.updated_at = datetime.today()
		models.storage.save()

    def to_dict(self):
        """
			Returns the dictionary BaseModel instance
			Has key value pair for representing class
		"""
        dictr = self.__dict__.copy()
        dictr["created_at"] = self.created_at.isoformat()
        dictr["updated_at"] = self.updated_at.isoformat()
        dictr["__class__"] = self.__class__.__name__
        return dictr

	def __str__(self):
        """
            Return print/string representation of Base Model
		"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
