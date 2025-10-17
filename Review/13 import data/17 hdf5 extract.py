import numpy as np
import h5py
import matplotlib.pyplot as plt

file = r'D:\STUDY\python\Review\13 import data\datasets\L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(file, 'r')

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = np.array(data['strain']['Strain'])

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
