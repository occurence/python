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
flights = spark.read.csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\24_Course_Machine_Learning_with_PySpark\datasets\flights_cross.csv',
                         sep=',',
                         header=True,
                         inferSchema=True,
                         nullValue='NA')

# flights = flights.limit(5000)

# flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0)) \
#                     .drop('mile')

# # Create 'label' column indicating whether flight delayed (1) or not (0)
# flights_km = flights_km.withColumn('label', when(flights_km.delay >= 15,1).otherwise(0).cast('integer'))

# Check first five records
# flights_km.show(5)

# # Convert categorical strings to index values
# indexer = StringIndexer(inputCol='org', outputCol='org_idx')

# # One-hot encode index values
# onehot = OneHotEncoder(
#     inputCols=['org_idx','dow'],
#     outputCols=['org_dummy','dow_dummy']
# )

# # Assemble predictors into a single column
# assembler = VectorAssembler(inputCols=['km','org_dummy','dow_dummy'], outputCol='features')

# # A linear regression object
# regression = LinearRegression(labelCol='duration')

# flights_train, flights_test = flights.randomSplit([0.8, 0.2], seed=43)
# print(flights_train.count())
# print(flights_test.count())
# flights_train.show(5)
# flights_test.show(5)

# # Import class for creating a pipeline
# from pyspark.ml import Pipeline

# # Construct a pipeline
# pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])

# # Train the pipeline on the training data
# pipeline = pipeline.fit(flights_train)

# # Make predictions on the testing data
# predictions = pipeline.transform(flights_test)

# # Create a confusion matrix, comparing predictions to known labels
# predictions.groupBy('duration', 'prediction').count().show()
# predictions.select('duration', 'prediction').show(5, False)
# print(pipeline.stages[3].intercept)
# print(pipeline.stages[3].coefficients)

# flights.show(5)

# flights_km = VectorAssembler(inputCols=['km'], outputCol='features').transform(flights)
# flights_km.show(5)
# flights_train, flights_test = flights_km.randomSplit([0.8, 0.2], seed=43)

# from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# # Create an empty parameter grid
# params = ParamGridBuilder().build()

# # Create objects for building and evaluating a regression model
# regression = LinearRegression(labelCol='duration')
# evaluator = RegressionEvaluator(labelCol='duration')

# # Create a cross validator
# cv = CrossValidator(estimator=regression, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)

# # Train and test model on multiple folds of the training data
# cv = cv.fit(flights_train)

# # NOTE: Since cross-valdiation builds multiple models, the fit() method can take a little while to complete.

# flights_train.show(5)
# flights_test.show(5)

# print(flights_train.count())
# print(flights_test.count())

flights.show(5)
# flights_train, flights_test = flights.randomSplit([0.8, 0.2], seed=43)
params = ParamGridBuilder().build()
regression = LinearRegression(labelCol='duration')
evaluator = RegressionEvaluator(labelCol='duration')

# Create an indexer for the org field
indexer = StringIndexer(inputCol='org', outputCol='org_idx')

# Create an one-hot encoder for the indexed org field
onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])

# Assemble the km and one-hot encoded fields
assembler = VectorAssembler(inputCols=['km', 'org_dummy'], outputCol='features')

# Create a pipeline and cross-validator.
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])
cv = CrossValidator(estimator=pipeline,
          estimatorParamMaps=params,
          evaluator=evaluator)

flights_train, flights_test = flights.randomSplit([0.8, 0.2], seed=43)
cv_model = cv.fit(flights_train)
predictions = cv_model.transform(flights_test)
predictions.select('duration', 'prediction').show(5)
print("Average cross-validated RMSE:", cv_model.avgMetrics)


flights.show(5)

flights_train.show(5)
flights_test.show(5)

print(flights_train.count())
print(flights_test.count())

# Create parameter grid
params = ParamGridBuilder()

# Add grids for two parameters
params = params.addGrid(regression.regParam, [0.01, 0.1, 1.0, 10.0]) \
               .addGrid(regression.elasticNetParam, [0.0, 0.5, 1.0])

# Build the parameter grid
params = params.build()
print('Number of models to be tested: ', len(params))

# Create cross-validator
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)