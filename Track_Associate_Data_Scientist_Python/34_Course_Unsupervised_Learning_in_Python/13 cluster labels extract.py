import numpy as np

mergings = np.array([[33.        , 36.        ,  0.27162909,  2.        ], [21.        , 26.        ,  0.31365739,  2.        ], [18.        , 43.        ,  0.32846589,  3.        ], [38.        , 41.        ,  0.34657328,  2.        ], [19.        , 22.        ,  0.37233454,  2.        ], [15.        , 27.        ,  0.38916958,  2.        ], [ 4.        , 11.        ,  0.48519909,  2.        ], [ 2.        , 13.        ,  0.60220511,  2.        ], [23.        , 25.        ,  0.64447995,  2.        ], [ 0.        ,  9.        ,  0.66671658,  2.        ], [32.        , 37.        ,  0.68359363,  2.        ], [39.        , 42.        ,  0.75541297,  3.        ], [12.        , 29.        ,  0.76129577,  2.        ], [30.        , 34.        ,  0.79066703,  2.        ], [24.        , 47.        ,  0.89015184,  3.        ], [ 1.        ,  6.        ,  0.96077742,  2.        ], [31.        , 45.        ,  0.98956619,  3.        ], [16.        , 50.        ,  1.05891757,  3.        ], [17.        , 20.        ,  1.11543099,  2.        ], [ 8.        , 40.        ,  1.13733735,  2.        ], [44.        , 46.        ,  1.1662041 ,  5.        ], [ 5.        , 61.        ,  1.28676337,  3.        ], [35.        , 52.        ,  1.37690488,  3.        ], [48.        , 49.        ,  1.52865125,  4.        ], [53.        , 64.        ,  1.66517195,  6.        ], [14.        , 56.        ,  1.74234784,  4.        ], [51.        , 65.        ,  1.91015424,  6.        ], [ 7.        , 57.        ,  1.91749035,  3.        ], [28.        , 55.        ,  2.08980038,  3.        ], [54.        , 58.        ,  2.13385537,  5.        ], [ 3.        , 10.        ,  2.22187038,  2.        ], [59.        , 67.        ,  2.31852251,  7.        ], [60.        , 62.        ,  2.33686195,  7.        ], [68.        , 69.        ,  2.76779035,  9.        ], [66.        , 70.        ,  3.13448417,  9.        ], [63.        , 71.        ,  3.25744652,  8.        ], [73.        , 74.        ,  3.71580316, 14.        ], [72.        , 75.        ,  4.68116988, 11.        ], [76.        , 77.        ,  5.45789312, 17.        ], [78.        , 79.        ,  6.74608427, 25.        ], [80.        , 81.        ,  9.61230238, 42.        ]])
varieties = ['Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Kama wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Rosa wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat', 'Canadian wheat']

# Perform the necessary imports
import pandas as pd
from scipy.cluster.hierarchy import fcluster

# Use fcluster to extract labels: labels
labels = fcluster(mergings, 6, criterion='distance')

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)