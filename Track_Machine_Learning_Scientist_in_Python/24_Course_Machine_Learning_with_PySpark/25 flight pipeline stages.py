from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import round, when

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

# flights = flights.limit(5000)

flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0)) \
                    .drop('mile')

# # Create 'label' column indicating whether flight delayed (1) or not (0)
# flights_km = flights_km.withColumn('label', when(flights_km.delay >= 15,1).otherwise(0).cast('integer'))

# Check first five records
flights_km.show(5)

# Convert categorical strings to index values
indexer = StringIndexer(inputCol='org', outputCol='org_idx')

# One-hot encode index values
onehot = OneHotEncoder(
    inputCols=['org_idx','dow'],
    outputCols=['org_dummy','dow_dummy']
)

# Assemble predictors into a single column
assembler = VectorAssembler(inputCols=['km','org_dummy','dow_dummy'], outputCol='features')

# A linear regression object
regression = LinearRegression(labelCol='duration')