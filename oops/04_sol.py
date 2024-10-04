# Polymorphism

class Car:
  def __init__(self, userbrand, usermodel):
    self.__brand = userbrand
    self.model = usermodel

  #  Encapsulation
  def get_brand(self):
    return self.__brand + " !"

  def full_name(self):
    return f"{self.__brand} {self.model} {self.battery_size}" 
# Polymorphism
  def fuel_type(self):
    return "Petrol and Diesel"


class ElectricCar(Car):
  def __init__(self,brand,model,battery_Size):
    super().__init__(brand, model)
    self.battery_size = battery_Size
# Polymorphism
  def fuel_type(self):
    return "Electric Charge"  


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())

my_toyota = Car("Toyota", "Etios")
print(my_toyota.fuel_type())