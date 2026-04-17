from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FlightsExample") \
    .getOrCreate()

csv_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\flights_small.csv"
flights_df = spark.read.csv(csv_path, header=True, inferSchema=True)
flights_df.createOrReplaceTempView("flights")
flights = spark.table("flights")

# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)

selected1.show()
selected2.show()