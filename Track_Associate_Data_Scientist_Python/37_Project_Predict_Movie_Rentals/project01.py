from datetime import datetime

# Define the datetime strings
dt1_string = "2005-05-28 23:40:33+00:00"
dt2_string = "2005-05-25 02:54:33+00:00"

# Convert the strings to datetime objects
dt1 = datetime.fromisoformat(dt1_string)
dt2 = datetime.fromisoformat(dt2_string)

# Subtract the two datetime objects
time_difference = dt1 - dt2

# Extract the number of days
days = time_difference.days

# Print the number of days
print("Number of days:", days)
