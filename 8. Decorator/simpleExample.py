"""
Decorator Concept Sample Code

"""

from abc import ABCMeta, abstractmethod
class IComponent(metaclass=ABCMeta):
    "Methods the component must implement"
    @staticmethod
    @abstractmethod
    def method():
        "A method to implement"

class Component(IComponent):
    "A component that can be decorated or not"
    def method(self):
        "An example method"
        return "Component Method"

class Decorator(IComponent):
    "The Decorator also implements the IComponent"
    def __init__(self, obj):
        "Set a reference to the decorated object"
        self.object = obj
    def method(self):
        "A method to implement"
        return f"Decorator Method({self.object.method()})"

# The Client
COMPONENT = Component()
print(COMPONENT.method())
print(Decorator(COMPONENT).method())


# Whant to augment an object with additional functionality
# Do not want to rewrite or alter existing code
# want to keep new functionality separate
# Neew to be able to interact with existing structures

#Decorator facilitates the addition of behaviors to individual objects without inheriting from them