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

planes_df = spark.read.csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\planes.csv", header=True, inferSchema=True)
planes_df = planes_df.withColumn("year",
    when(col("year") == "NA", None).otherwise(col("year")).cast("float")
)
planes_df.createOrReplaceTempView("planes")
planes = spark.table("planes")

# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")

print(model_data.show())