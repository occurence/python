import random

class MockStock:
    def __init__(self, loc, scale):
        """
        Initialize the MockStock object.

        Parameters:
        loc (float): The base price of the stock.
        scale (float): A scaling factor for simulating price fluctuations.
        """
        self.loc = loc
        self.scale = scale

    def price(self):
        """
        Simulate the stock price.

        Returns:
        float: A random stock price based on the loc and scale.
        """
        return round(random.gauss(self.loc, self.scale), 2)  # Gaussian distribution for mock prices


import contextlib

@contextlib.contextmanager
def stock(symbol):
  base = 140.00
  scale = 1.0
  mock = MockStock(base, scale)
  print('Opening stock ticker for {}'.format(symbol))
  yield mock
  print('Closing stock ticker')

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\24_Course_Writing_Functions_in_Python\datasets\NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))