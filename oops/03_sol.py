# Encapsulation

class Car:
  def __init__(self, userbrand, usermodel):
    self.__brand = userbrand
    self.model = usermodel

  #  Encapsulation
  def get_brand(self):
    return self.__brand + " !"

  def full_name(self):
    return f"{self.__brand} {self.model} {self.battery_size}" 


class ElectricCar(Car):
  def __init__(self,brand,model,battery_Size):
    super().__init__(brand, model)
    self.battery_size = battery_Size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand) // direct access not allowed
print(my_tesla.get_brand())