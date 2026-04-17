from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FlightsExample") \
    .getOrCreate()

csv_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\flights_small.csv"
flights_df = spark.read.csv(csv_path, header=True, inferSchema=True)
flights_df.createOrReplaceTempView("flights")

# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())