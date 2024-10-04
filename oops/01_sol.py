#class
class Car:
  #constructor
  def __init__(self, userbrand, usermodel):
    self.brand = userbrand
    self.model = usermodel

  def full_name(self):
    return f"{self.brand} {self.model}"  
  
# object
my_car = Car("Toyota","Etios_liva")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())    
