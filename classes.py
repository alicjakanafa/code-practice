# class Greeter():
#     def hello(self):
#         return "Hello!"

#     def good_bye(self):
#         return "Good bye!"

# greeter = Greeter()
# print(greeter.hello())
# print(greeter.good_bye())

# class Greeter():
#     def __init__(self):
#         print("Hello! I am a Greeter class!")

# new = Greeter()

class Country():
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        print(f"{self.name} has a capital called {self.capital} and a population of {self.population}.")

country = Country("England", "London", 56000000)

class Person():
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        print(f"{self.name} is {self.age} years old and is {self.nationality}.")

person = Person("John Doe", 30, "American")

class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        print(f"{self.name} is a {self.breed} and is {self.age} years old.")

dog = Dog("Buddy", "Golden Retriever", 3)

class Animal():
    def __init__(self, species, habitat, diet):
        self.species = species
        self.habitat = habitat
        self.diet = diet
        print(f"The {self.species} lives in {self.habitat} and has a {self.diet} diet.")

animal = Animal("Lion", "Savannah", "Carnivorous")
animal2 = Animal("Elephant", "Forest", "Herbivorous")

class Plant():
    def __init__(self, name, type, height):
        self.name = name
        self.type = type
        self.height = height
        print(f"The {self.name} is a {self.type} and can grow up to {self.height} meters tall.")

plant = Plant("Rose", "Flower", 1.5)
plant2 = Plant("Oak", "Tree", 20)

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"The car is a {self.year} {self.make} {self.model}.")

car = Car("Toyota", "Camry", 2020)

class Superhero():
    def __init__(self, name, superpower, nemesis):
        self.name = name
        self.superpower = superpower
        self.nemesis = nemesis
        print(f"{self.name} has the superpower of {self.superpower} and their nemesis is {self.nemesis}.")

superhero = Superhero("Spider-Man", "Wall-Crawling", "Green Goblin")
superhero2 = Superhero("Batman", "Detective Skills", "Joker")

class Supervillain():
    def __init__(self, name, evil_plan, weakness):
        self.name = name
        self.evil_plan = evil_plan
        self.weakness = weakness
        print(f"{self.name} has an evil plan to {self.evil_plan} and their weakness is {self.weakness}.")

supervillain = Supervillain("Thanos", "Collect all Infinity Stones", "Pride")
supervillain2 = Supervillain("Lex Luthor", "World Domination", "Arrogance")

# class Person():
#      def __init__(self, first_name, surname):
#          # note that we're not using instance variables here
#          first_name = first_name
#          surname = surname

#      def full_name(self):
#          # will this work without using instance variables above?
#          return f"{first_name} {surname}"

# alan_turing = Person("Alan", "Turing")
# alan_turing.full_name()

# what gets returned here?
# We get an error because the instance variables are not being set in the constructor. The `full_name` method is trying to access `first_name` and `surname`, which are not defined as instance variables. To fix this, we should use `self.first_name` and `self.surname` in the constructor and in the `full_name` method.

# Corrected code:
class Person():
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def full_name(self):
        return f"{self.first_name} {self.surname}"
    
alan_turing = Person("Alan", "Turing")
print(alan_turing.full_name())  # This will now correctly return "Alan Turing