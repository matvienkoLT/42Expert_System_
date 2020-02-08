from enum import Enum

class NodeType(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Node:
    def __init__(self, type, name, statement):
        self.__type = type
        self.__name = name
        self.__statement = statement
        self.__child = None

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def statement(self):
        return self.__statement

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
       if isinstance(value, Node):
           self.__child = value
       else:
            raise Exception("Go Fuck yourself, asshole")

    @child.deleter
    def child(self):
        self.__child = None
