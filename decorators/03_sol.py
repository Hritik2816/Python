
import time

def cache(func):
  cache_value = {}
  print(cache_value)
  def wrapper(*args):
    if args in cache_value:
      return cache_value[args]
    result = func(*args)
    cache_value[args] = result
    return result
  return wrapper



@cache
def lon_running_function(a, b):
  time.sleep(4)
  return a + b

print(lon_running_function(2,9))
print(lon_running_function(2,9))
print(lon_running_function(4,5))
