#!/usr/bin/python3

"""class will be the “base”
 of all other classes in this project"""
import json


class Base:
    """parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_objs):
        if list_objs is None or len(list_objs) == 0:
            return "[]"

        if isinstance(list_objs[0], dict):
            return json.dumps(list_objs)
        else:
            return json.dumps([obj.to_dictionary() for obj in list_objs])

    @staticmethod
    def save_to_file(list_objs):
        filename = list_objs[0].__class__.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of Base objects from a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
