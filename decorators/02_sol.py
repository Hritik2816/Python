# Debug

def deburg(func):
  def wrapper(*args,**kwargs ):
    args_value = ", ".join(str(arg) for arg in args)
    kwargs_value = ", ".join(f"{k}={v}"for k, v in kwargs.items())
    print(f"calling: {func.__name__} with args {args_value} and kwagrs {kwargs_value}")
    return func(*args,**kwargs)

  return wrapper  




# Make first road just for fun...
@deburg
def greet(name, greeting="Hello"):
  print(f"{greeting} {name}")

greet("Hritik", greeting = "HaaJi ")  