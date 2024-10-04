# isInstance

class Car:
  total_car = 0
  def __init__(self, userbrand, usermodel):
    self.__brand = userbrand
    self.__model = usermodel
    Car.total_car += 1

  #  Encapsulation
  def get_brand(self):
    return self.__brand + " !"

  def full_name(self):
    return f"{self.__brand} {self.__model} {self.battery_size}" 
  # Polymorphism
  def fuel_type(self):
    return "Petrol and Diesel"
  #Static Method also we can say that decorator also no need of self
  @staticmethod
  def general_discription():
    return "Cars are means of transport"
  # Property doesn't change also used same name
  @property
  def model(self):
    return self.__model



class ElectricCar(Car):
  def __init__(self,brand,model,battery_Size):
    super().__init__(brand, model)
    self.battery_size = battery_Size
# Polymorphism
  def fuel_type(self):
    return "Electric Charge"  


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
# print(my_tesla.fuel_type())

# my_toyota = Car("Toyota", "Etios")
# print(my_toyota.fuel_type())

# print(Car.general_discription()) 

# print(my_toyota.model)
