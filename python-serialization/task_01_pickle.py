#!/usr/bin/python3
"""
Module for learning how to serialize and deserialize custom
Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """custom Python class"""

    def __init__(self, name, age, is_student):
        """initialize the CustomObject instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print out the object's attributes"""
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Is Student: ", self.is_student)

    def serialize(self, filename):
        """
        take a filename as its parameter. Using the pickle module,
        it will serialize the current instance of the object and save
        it to the provided filename.
        """
        try:
            with open(filename, "wb")as file:
                pickle.dump(self, file)
            return True
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        take a filename as its parameter. Using the pickle module, it
        will load and return an instance of the CustomObject from the
        provided filename.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)

            if isinstance(obj, cls):
                return obj
            return None

        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
