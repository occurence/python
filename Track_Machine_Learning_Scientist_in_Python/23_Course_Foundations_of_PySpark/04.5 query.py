from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FlightsExample") \
    .getOrCreate()

csv_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\flights_small.csv"
flights_df = spark.read.csv(csv_path, header=True, inferSchema=True)
flights_df.createOrReplaceTempView("flights")

# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()