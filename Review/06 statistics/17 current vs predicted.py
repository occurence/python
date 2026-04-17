import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

print(100 - norm.cdf(1000, 5000, 2000) * 100)
print(100 - norm.cdf(1000, 6000, 2600) * 100)