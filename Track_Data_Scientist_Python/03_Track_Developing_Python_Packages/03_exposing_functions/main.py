import sys
import os

# Add the parent directory of impyrial to the import path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import impyrial

print("impyrial file:", getattr(impyrial, '__file__', 'NO __file__'))
print("impyrial dir:", dir(impyrial))
print("length module:", impyrial.length)
