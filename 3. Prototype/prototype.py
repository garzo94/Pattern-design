# how to make a prototype:, (copy a object and customize it)

import copy


class Address:
    def __init__(self, street_address, city, suite):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.suite}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


addres =  Address("123 London Road", "London", "UK")
john = Person("John", addres)
jane =  Person('Jane', addres)
# If change the adress to jane also change it to john, because is the same instance for both
jane.address.street_address = "123B London Road"
print(john, jane)

# to solve this we use copy.deepcoy() records a copy of all the attributes, maaking a new object
jane = copy.deepcopy(john)
jane.address.street_address = '124 London Road'
print(john,jane)

