import pandas as pd

used_cars = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\cars_rating.csv')

used_cars_updated = used_cars[['color', 'engine_fuel', 'transmission', 'price_usd']].copy()
used_cars_updated[['color', 'engine_fuel', 'transmission']] = used_cars_updated[['color', 'engine_fuel', 'transmission']].astype('category')
used_cars_updated[['color', 'engine_fuel', 'transmission']] = used_cars_updated[['color', 'engine_fuel', 'transmission']].apply(lambda x: x.cat.codes)

color_map = dict(zip(used_cars_updated['color'], used_cars['color']))
fuel_map = dict(zip(used_cars_updated['engine_fuel'], used_cars['engine_fuel']))
transmission_map = dict(zip(used_cars_updated['transmission'], used_cars['transmission']))
print(used_cars_updated.head(3))

# Update the color column using the color_map
used_cars_updated["color"] = used_cars_updated["color"].map(color_map)
# Update the engine fuel column using the fuel_map
used_cars_updated["engine_fuel"] = used_cars_updated["engine_fuel"].map(fuel_map)
# Update the transmission column using the transmission_map
used_cars_updated["transmission"] = used_cars_updated["transmission"].map(transmission_map)

# Print the info statement
print(used_cars_updated.info())

print(used_cars_updated.head(3))