from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FlightsExample") \
    .getOrCreate()

csv_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\flights_small.csv"
flights_df = spark.read.csv(csv_path, header=True, inferSchema=True)
flights_df.createOrReplaceTempView("flights")

# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
flights.show()

# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time/60)

# Show the head
flights.show()