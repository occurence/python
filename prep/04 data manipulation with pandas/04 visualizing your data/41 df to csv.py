"""
DataFrame to CSV
You're almost there! To make things easier to read, you'll need to sort the data and export it to CSV so that your colleagues can read it.

pandas as pd has been imported for you.
"""

# Sort airline_totals by the values of bumps_per_10k from highest to lowest, storing as airline_totals_sorted.
# Print your sorted DataFrame.
# Save the sorted DataFrame as a CSV called "airline_totals_sorted.csv".

import pandas as pd
airline_bumping = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\airline_bumping.csv")
airline_totals = airline_bumping.groupby('airline')[['nb_bumped','total_passengers']].sum()
airline_totals["bumps_per_10k"] = airline_totals['nb_bumped'] / airline_totals['total_passengers'] * 10000

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k', ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\airline_totals_sorted.csv")

# Excellent exporting! 
# Now you can share these insights about your competitors with your team.