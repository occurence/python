from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder \
    .appName("FlightsExample") \
    .getOrCreate()

flights_df = spark.read.csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\flights_small.csv", header=True, inferSchema=True)
flights_df = flights_df.withColumn("air_time",
    when(col("air_time") == "NA", None).otherwise(col("air_time")).cast("float")
).withColumn("dep_delay",
    when(col("dep_delay") == "NA", None).otherwise(col("dep_delay")).cast("float")
)
flights_df.createOrReplaceTempView("flights")
flights = spark.table("flights")

airports_df = spark.read.csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\airports.csv", header=True, inferSchema=True)
airports_df.createOrReplaceTempView("airports")
airports = spark.table("airports")

# Examine the data
print(airports.show())

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")

# Examine the new DataFrame
print(flights_with_airports.show())