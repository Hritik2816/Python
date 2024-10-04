# Inheritance

class Car:
  def __init__(self, userbrand, usermodel):
    self.brand = userbrand
    self.model = usermodel

  def full_name(self):
    return f"{self.brand} {self.model} {self.battery_size}" 

# Inheritance
class ElectricCar(Car):
  def __init__(self,brand,model,battery_Size):
    super().__init__(brand, model)
    self.battery_size = battery_Size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.full_name())