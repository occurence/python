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
planes = planes.withColumnRenamed("year", "plane_year")

model_data = flights.withColumn("arr_delay", flights.arr_delay.cast("integer"))
model_data = flights.withColumn("air_time", flights.air_time.cast("integer"))
model_data = flights.withColumn("month", flights.month.cast("integer"))
model_data = planes.withColumn("plane_year", planes.plane_year.cast("integer"))

model_data = flights.join(planes, on="tailnum", how="leftouter")

model_data = model_data.withColumn("plane_age", flights.year - planes.plane_year)

# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")

# model_data.show()

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import OneHotEncoder

# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")

# Create a StringIndexer
dest_indexer = StringIndexer(inputCol="dest", outputCol="dest_index")

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")

from pyspark.ml.feature import VectorAssembler

# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")

# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])

# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)