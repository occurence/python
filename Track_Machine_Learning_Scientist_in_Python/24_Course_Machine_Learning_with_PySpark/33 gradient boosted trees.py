from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import round, when
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder


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

# Remove the 'flight' column
flights = flights.drop('flight')

# Number of records with missing 'delay' values
flights.filter('delay IS NULL').count()

# Remove records with missing 'delay' values
flights = flights.filter('delay IS NOT NULL')

# Remove records with missing values in any column and get the number of remaining rows
flights = flights.dropna()
print(flights.count())

# flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0)) \
#                     .drop('mile')

# Create 'label' column indicating whether flight delayed (1) or not (0)
flights = flights.withColumn('label', when(flights.delay >= 15,1).otherwise(0).cast('integer'))

# Check first five records
flights.show(5)

assembler = VectorAssembler(inputCols=[
    'mon','depart','duration'
], outputCol='features')

# Consolidate predictor columns
flights = assembler.transform(flights)

# Check the resulting column
flights.select('mon','depart','duration','features','label').show(5, truncate=False)

flights_train, flights_test = flights.randomSplit([0.8, 0.2], seed=43)
print(flights_train.count())
print(flights_test.count())

# Import the classes required
from pyspark.ml.classification import DecisionTreeClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Create model objects and train on training data
tree = DecisionTreeClassifier().fit(flights_train)
gbt = GBTClassifier().fit(flights_train)

# Compare AUC on testing data
evaluator = BinaryClassificationEvaluator()
print(evaluator.evaluate(tree.transform(flights_test)))
print(evaluator.evaluate(gbt.transform(flights_test)))

# Find the number of trees and the relative importance of features
print(gbt.trees)
print(gbt.featureImportances)