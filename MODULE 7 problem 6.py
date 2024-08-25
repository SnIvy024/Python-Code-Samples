# Your Name: Ivette Mujica
# The Date: 08/23/2024
# Problem 6 - This problem I Modify the car class to add attributes for the type and manufacturer and update them basically just class them this was really hard 

class car:
    def __init__(self, model, year, color, car_type, manufacturer):
       
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.car_type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
       
        return f"{self.manufacturer} {self.model} ({self.car_type}) - {self.year} - {self.color}"

# Creating a car with objects and new attributes

car1 = car("Sports", 2012, "Blue", "Coupe", "Ferrari")
car2 = car("Sedan", 2020, "Black", "Saloon", "Toyota")

# Printing out various attributes and full specifications

print(car1.get_color())       
  # puts Blue
print(car1.get_model())      
   # puts Sports
print(car2.get_color())        
 # puts Black
print(car1.get_type())         
 # puts Coupe
print(car2.get_manufacturer())
 # puts Toyota
print(car1.fullspecs())      
 # puts Ferrari Sports (Coupe) - 2012 - Blue
print(car2.fullspecs())       
# puts Toyota Sedan (Saloon) - 2020 - Black
