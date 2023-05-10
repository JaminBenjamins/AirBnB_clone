#!/usr/bin/python3
""" Define a class that stores objects """
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
	""" A representation of data storage abstraction
	
	Attributes:
		_file_path (str): The path to save objects
		_objects (dict): A dictionary object
	"""
	
	__file_path = "file.json"
	__objects = {}

	def all(self):
	    """ Returns a dictionary of objects """
        return FileStorage.__objects
	
	def new(self, obj):
	    """ Sets in __objects with the class name as key """
        ocname = obj.__class__.__name__
	FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

	def save(self):
        """ Serialize __objects to the JSON file __file_path """
	odict = FileStorage.__objects
	objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
	with open(FileStorage.__file_path, "w") as f:
		json.dumps(objdict, f)

	def reload(self):
		""" Deserialize the JSON file __file_path to the respective object """
		try:
			with open(FileStorage.__file_path) as f:
				objdict = json.load(f)
				for o in objdict.values():
					cls_name = o["__class__"]
					del o["__class__"]
					self.new(eval(cls_name)(**o))
		except FileNotFoundError:
			return
