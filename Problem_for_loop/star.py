
def rightPattern(n):
  for i in range(n):
    for j in range(i+1):
      print("*", end=" ")
    print("")
rightPattern(5)    
print("\n")

def diffAngle(n):
  for i in range(n):
    for j in range(i,n):
      print("*", end=" ")
    print("")
diffAngle(5)  
print("\n")

def rightSideTriangle(n):
  for i in range(n):
    for j in range(i,n):
      print(" ", end=" ") #Spacing are very important
    for j in range(i+1):
      print("*", end=" ")
    print()
rightSideTriangle(5)      
print("\n")


def rightSidedTriangle(n):
  for i in range(n):
    for j in range(i+1):
      print(" ", end=" ")
    for j in range(i,n):
      print("*", end=" ")
    print()
rightSidedTriangle(5)     
print("\n")

def Hilltriangle(n):
  for i in range(n):
    for j in range(i,n):
      print(" ", end=" ")
    for j in range(i):
      print("*", end=" ")
    for j in range(i+1):
      print("*", end=" ")
    print()
Hilltriangle(5)
print("\n")      

def revHillTriangle(n):
  for i in range(n):
    for j in range(i + 1):
      print(" ", end=" ")
    for j in range(i,n-1):
      print("*", end=" ")
    for j in range(i,n):
      print("*", end=" ")
    print()
revHillTriangle(5)      
print("\n")

def diamond(n):
  for i in range(n-1):
    for j in range(i,n):
      print(" ", end=" ")
    for j in range(i):
      print("*", end=" ")
    for j in range(i+1):
      print("*", end=" ")
    print()  
  for i in range(n):
    for j in range(i+1):
      print(" ", end=" ")
    for j in range(i,n-1):
      print("*", end=" ")
    for j in range(i,n):
      print("*", end=" ")
    print()
diamond(5)      
print("\n")

def butterfly(n):
    for i in range(n):
      for j in range(i + 1):
        print(" ", end=" ")
      for j in range(i,n-1):
        print("*", end=" ")
      for j in range(i,n):
        print("*", end=" ")
      print()
    for i in range(n):
      for j in range(i,n):
        print(" ", end=" ")
      for j in range(i):
        print("*", end=" ")
      for j in range(i+1):
        print("*", end=" ")
      print() 
butterfly(5)       