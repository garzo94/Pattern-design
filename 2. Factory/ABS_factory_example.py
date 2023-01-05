from abc import ABC, abstractmethod

class IPerson(ABC):
    @abstractmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):
    def __init__(self) -> None:
        self.name = "some name"

    def person_method(self):
        print('I am a student')

class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Teacher Name"

    def person_method():
        print('I am a teacher')

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")


person = PersonFactory.build_person('Student')
person.person_method()
# output
# I am a student


