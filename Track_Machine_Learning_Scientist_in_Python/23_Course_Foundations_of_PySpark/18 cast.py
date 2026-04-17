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

flights = flights.withColumnRenamed("year", "plane_year")

# Cast the columns to integers
model_data = flights.withColumn("arr_delay", flights.arr_delay.cast("integer"))
model_data = flights.withColumn("air_time", flights.air_time.cast("integer"))
model_data = flights.withColumn("month", flights.month.cast("integer"))
model_data = flights.withColumn("plane_year", flights.plane_year.cast("integer"))

model_data.show()