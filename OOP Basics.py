# Classes are blueprints for objects. We create a blueprint and from a blueprint/class, we create
# an object. Classes are always created with first letters capitalized.
# All classes serve as our basis for creating objects. Here we define the general properties/attributes
# and actions that class will have and then objects with uniqueness can come out of them.
# All objects we create in python are objects of classes i.e belong to a class. When we create a class
# object from its blueprint class, the object has the general properties & methods of the class.
# An object of a list class has the general properties and methods of the list class.
# When we create an object in python either a string, list, dictionary whatsoever, also has the general
# properties and methods of the class/blueprint it belongs to. For instance, a new list cars when created
# inherits the methods as well as properties of the class 'list'. That makes python object-oriented in
# its nature where different kind of objects can be created from existing classes.


# ---- CREATING THE CARS OBJECT FROM LIST CLASS--------
# cars = []
# print(type(cars))
# from books import Books
# mybook = Books()
# mybook.displayChapterSize()
#
# input()
#

class Country:
    def __init__(self,name,capital,flagcolor):
        self.name = name
        self.capital = capital
        self.flagcolor = flagcolor
    def warCommand(self,s):
        print(s)
        return 'Aye'



country1 = Country('Germany','Berlin','Black & White')
country2 = Country('Nigeria','Abuja','Green & White')
country3 = Country('Kenya','Nairobi','Red & Black')
print(isinstance(country1,Country))
print(country1.name)
print(country1.flagcolor)
print(country3.warCommand('Retreat'))
print(country1)


country1.landmass = 5000
print(country1.landmass)
print(country2.landmass) # attribute needs to be defined. landmass attribute for country2
# not defined


print(country1.warCommand('Attack'))
country2.landmass = 6400
print(country2.flagcolor)
print(country2.landmass)
print(isinstance(country1, Country))


