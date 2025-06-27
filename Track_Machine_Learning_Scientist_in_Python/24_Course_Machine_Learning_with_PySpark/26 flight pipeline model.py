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

flights_train, flights_test = flights_km.randomSplit([0.8, 0.2], seed=43)
print(flights_train.count())
print(flights_test.count())
flights_train.show(5)
flights_test.show(5)

# Import class for creating a pipeline
from pyspark.ml import Pipeline

# Construct a pipeline
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])

# Train the pipeline on the training data
pipeline = pipeline.fit(flights_train)

# Make predictions on the testing data
predictions = pipeline.transform(flights_test)

# Create a confusion matrix, comparing predictions to known labels
predictions.groupBy('duration', 'prediction').count().show()
predictions.select('duration', 'prediction').show(5, False)
print(pipeline.stages[3].intercept)
print(pipeline.stages[3].coefficients)