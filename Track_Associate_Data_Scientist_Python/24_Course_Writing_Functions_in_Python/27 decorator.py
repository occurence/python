import inspect

def print_args(func):
  sig = inspect.signature(func)
  def wrapper(*args, **kwargs):
    bound = sig.bind(*args, **kwargs).arguments
    str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
    print('{} was called with {}'.format(func.__name__, str_args))
    return func(*args, **kwargs)
  return wrapper

def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)

my_function(1, 2, 3)