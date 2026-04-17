from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder \
    .appName("FlightsExample") \
    .getOrCreate()

csv_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\flights_small.csv"
flights_df = spark.read.csv(csv_path, header=True, inferSchema=True)
flights_df = flights_df.withColumn("air_time",
    when(col("air_time") == "NA", None).otherwise(col("air_time")).cast("float")
)
flights_df.createOrReplaceTempView("flights")
flights = spark.table("flights")

# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()