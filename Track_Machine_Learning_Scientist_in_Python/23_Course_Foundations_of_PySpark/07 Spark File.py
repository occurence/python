import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print(spark)

# Don't change this file path
file_path = r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\23_Course_Foundations_of_PySpark\datasets\airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()