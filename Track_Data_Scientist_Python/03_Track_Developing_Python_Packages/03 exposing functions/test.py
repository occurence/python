# main.py
import impyrial

# This should now be accessible
print(dir(impyrial))            # should contain 'length'
print(impyrial.length)          # should not throw AttributeError
