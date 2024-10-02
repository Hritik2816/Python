import math

def circle(radius):
  area = math.pi * radius ** 2
  circum = 2 * math.pi * radius
  floored_area = math.floor(area*100)/100
  floored_circum = math.floor(circum*100)/100

  return floored_area, floored_circum

a, c = circle(4)

print("Area: ",a, "\nCircumfrence: ",c)
