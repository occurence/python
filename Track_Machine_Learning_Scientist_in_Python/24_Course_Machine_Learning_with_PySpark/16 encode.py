from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()

# Read data from CSV file
flights = spark.read.csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\24_Course_Machine_Learning_with_PySpark\datasets\flights.csv',
                         sep=',',
                         header=True,
                         inferSchema=True,
                         nullValue='NA')

from pyspark.ml.feature import StringIndexer

# Repeat the process for the other categorical feature
flights = StringIndexer(inputCol='org', outputCol='org_idx').fit(flights).transform(flights)
flights.show(5)

# Import the one hot encoder class
from pyspark.ml.feature import OneHotEncoder

# Create an instance of the one hot encoder
onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])

# Apply the one hot encoder to the flights data
onehot = onehot.fit(flights)
flights_onehot = onehot.transform(flights)

# Check the results
flights_onehot.select('org', 'org_idx', 'org_dummy').distinct().sort('org_idx').show()

spark.stop()