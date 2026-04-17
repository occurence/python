import pandas as pd

used_cars_updated = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\cars_code.csv')
color_map = {1: 'other', 0: 'black', 2: 'white'}
fuel_map = {3: 'gasoline', 2: 'gas', 0: 'diesel', 5: 'hybrid-petrol', 4: 'hybrid-diesel', 1: 'electric'}
transmission_map = {0: 'automatic', 1: 'mechanical'}

# Update the color column using the color_map
used_cars_updated["color"] = used_cars_updated['color'].map(color_map)
# Update the engine fuel column using the fuel_map
used_cars_updated["engine_fuel"] = used_cars_updated['engine_fuel'].map(fuel_map)
# Update the transmission column using the transmission_map
used_cars_updated["transmission"] = used_cars_updated['transmission'].map(transmission_map)

# Print the info statement
print(used_cars_updated.info())