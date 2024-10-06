# Decorators
# func in func then pass argument also this sytax used every where 

import time

# This is toll tax
def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} ran in {end-start} time")
    return result
  return wrapper

@timer
# Timer decoeator help to alway you go through then toll tax
def example_function(n):
  time.sleep(n)

example_function(2)  