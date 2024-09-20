# class Car:
#     def __init__(self,color,make,model,fuel_type):
#         self.color = color
#         self.make = make
#         self.model = model
#         self.fuel_type = fuel_type
    
#     def name_of_car(self):
#         long_name = f"{self.color} {self.make} {self.model} {self.fuel_type}"
#         print(f"My car is a {long_name}")

# car1 = Car("Yellow","Ford","Mustang","Gasoline")
# car2 = Car("Red","Toyota","Prius","Hybrid")
# car3 = Car("Blue","Volkswagon","Golf","Diesel")

# # car1.name_of_car()
# # car2.name_of_car()
# # car3.name_of_car()


# class Dog:
    
#     def __init__(self,name,breed):
#         self._name = name #makes attribute "private" meaning it cant be accessed from outside the class
#         self._breed = breed

#     def __str__(self):
#         return f"{self._name} {self._breed}"
#         # return self.breed
    
#     def bark(self):
#         print(f"{self.name} {self.breed} barked!")

#     def giveMeAttributes(self):
#         print(f"{self.name} {self.breed}")
    
#     def changeBreed(self,new_breed):
#         self._breed = new_breed
    
#     def giveBreed(self):
#         print(self._breed)

# dog_1.changeBreed("husky")
# dog_1 = Dog("Firulais","Chihuahua")
# dog_2 = Dog("Golden", "Retriever")
# print(dog_1)
# # dog_1.bark()
# # dog_1.giveMeAttributes()
# print(dog_2)
# # dog_2.bark()
# # dog_2.giveMeAttributes()



# class Pet:
#     def __init__(self,name):
#         self.name = name
    
#     def __str__(self):
#         return self.name

#     def get_name(self):
#         return self.name

# class Home:

#     def __init__(self,owner):
#         self._owner = owner
#         self._pets = []

#     def __str__(self):
#         return f"Home Owner: {self._owner}"

#     def adopt_pet(self, pet_object):
#         self._pets.append(pet_object)

#     def show_pets(self):
#         return self._pets

# pet_one = Pet('Mittens')
# my_home = Home("Gary")

# print(pet_one, my_home)
# print(my_home.show_pets())
# my_home.adopt_pet(pet_one)
# for pet in my_home.self_pets:
#     print(pet)
# # print(my_home.show_pets())
class Club:
    def __init__(self, title):
        self._title = title
    def get_title(self):
        return self._title
    
class ClubAssociation:
    def __init__(self):
        self._recognized_clubs = []
    def add_new_club(self, title):
        new_club_object = Club(title)
        self._recognized_clubs.append(new_club_object)
    def list_available_club(self):
        print(self._recognized_clubs)
    def check_title(self, checkedTitle):
        for club_object in self._recognized_clubs:
            if club_object.get_title() == checkedTitle:
                print('Yes that is a recognized club.')

my_club_association = ClubAssociation()
my_club_association.add_new_club('Chess')
my_club_association.add_new_club('The Baker Street Irregulars')
my_club_association.add_new_club('Food for thought')
my_club_association.list_available_club()
my_club_association.check_title('Photography')

"""
class Club:
    def __init__(self, title):
        self._title = title
    def get_title(self):
        return self._title
    
class ClubAssociation:
    def __init__(self):
        self._recognized_clubs = []
    def add_new_club(self, title):
        new_club_object = Club(title)
        self._recognized_clubs.append(new_club_object)
    def list_available_club(self):
        print(self._recognized_clubs)
    def check_title(self, checkedTitle):
        for club_object in self._recognized_clubs:
            if club_object.get_title() == checkedTitle:
                print('Yes that is a recognized club.')

my_club_association = ClubAssociation()
my_club_association.add_new_club('Chess')
my_club_association.add_new_club('The Baker Street Irregulars')
my_club_association.add_new_club('Food for thought')
my_club_association.list_available_club()
my_club_association.check_title('Photography')
"""