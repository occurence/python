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

# flights = flights.limit(5000)

# # Remove the 'flight' column
# flights_drop_column = flights.drop('flight')

# # Number of records with missing 'delay' values
# flights_drop_column.filter('delay IS NULL').count()

# # Remove records with missing 'delay' values
# flights_valid_delay = flights_drop_column.filter('delay IS NOT NULL')

# # Remove records with missing values in any column and get the number of remaining rows
# flights_none_missing = flights_valid_delay.dropna()
# print(flights_none_missing.count())

# Import the required function
from pyspark.sql.functions import round, when

# Convert 'mile' to 'km' and drop 'mile' column (1 mile is equivalent to 1.60934 km)
# flights_km = flights_none_missing.withColumn('km', round(flights_none_missing.mile * 1.60934, 0)) \
flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0)) \
                    .drop('mile')

# # Create 'label' column indicating whether flight delayed (1) or not (0)
# flights_km = flights_km.withColumn('label', when(flights_km.delay >= 15,1).otherwise(0).cast('integer'))

# Check first five records
flights_km.show(5)

from pyspark.ml.feature import StringIndexer
# Import the one hot encoder class
from pyspark.ml.feature import OneHotEncoder

# Create an indexer
carrier_indexer = StringIndexer(inputCol='carrier', outputCol='carrier_idx')
carrier_encoded = OneHotEncoder(inputCol="carrier_idx", outputCol="carrier_dummy")

# Indexer identifies categories in the data
indexer_model = carrier_indexer.fit(flights_km)

# Indexer creates a new column with numeric index values
flights_indexed = indexer_model.transform(flights_km)

# Repeat the process for the other categorical feature
flights_indexed = StringIndexer(inputCol='org', outputCol='org_idx').fit(flights_indexed).transform(flights_indexed)
flights_indexed.show(5)

# Import the one hot encoder class
from pyspark.ml.feature import OneHotEncoder

# Create an instance of the one hot encoder
# onehot = OneHotEncoder(inputCols=['org_idx'], outputCols=['org_dummy'])
onehot = OneHotEncoder(inputCols=['carrier_idx','org_idx'], outputCols=['carrier_dummy','org_dummy'])

# Apply the one hot encoder to the flights data
onehot = onehot.fit(flights_indexed)
flights_onehot = onehot.transform(flights_indexed)

# Check the results
flights_onehot.select('org', 'org_idx', 'org_dummy').distinct().sort('org_idx').show()

# Import the necessary class
from pyspark.ml.feature import VectorAssembler

# Create an assembler object
assembler = VectorAssembler(inputCols=[
    # 'mon','dom','dow','carrier_idx','org_idx','km','depart','duration','km'
    # 'km','carrier_dummy'
    'km','org_dummy'
], outputCol='features')

# Consolidate predictor columns
flights_assembled = assembler.transform(flights_onehot)

# Check the resulting column
# flights_assembled.select('features', 'delay').show(5, truncate=False)
flights_assembled.select('km','features','duration').show(5, truncate=False)

# flights_assembled.select('mon','dom','dow','carrier_idx','org_idx','km','depart','duration', 'features', 'delay').show(5, truncate=False)
flights_assembled.select('mon','dom','dow','carrier','flight','org','depart','duration','delay','km','org_idx','org_dummy','features').show(5, truncate=False)
flights_assembled.select('km','org_idx','org_dummy','features').show(5, truncate=False)

# Split into training and testing sets in a 80:20 ratio
flights_train, flights_test = flights_assembled.randomSplit([0.8, 0.2], seed=43)

# Check that training set has around 80% of records
training_ratio = flights_train.count() / flights_assembled.count()
print(training_ratio)

# # Import the Decision Tree Classifier class
# from pyspark.ml.classification import DecisionTreeClassifier

# # Create a classifier object and fit to the training data
# tree = DecisionTreeClassifier()
# tree_model = tree.fit(flights_train)

# # Create predictions for the testing data and take a look at the predictions
# prediction = tree_model.transform(flights_test)
# prediction.select('label', 'prediction', 'probability').show(5, False)

# # Create a confusion matrix
# prediction.groupBy('label', 'prediction').count().show()

# # Calculate the elements of the confusion matrix
# TN = prediction.filter('prediction = 0 AND label = prediction').count()
# TP = prediction.filter('prediction = 1 AND label = prediction').count()
# FN = prediction.filter('prediction = 0 AND label != prediction').count()
# FP = prediction.filter('prediction = 1 AND label != prediction').count()

# # Accuracy measures the proportion of correct predictions
# accuracy = (TN + TP) / (TN + TP + FN + FP)
# print(accuracy)

print(flights_train.count())
print(flights_test.count())

flights_train.show()
flights_test.show()

# # Import the logistic regression class
# from pyspark.ml.classification import LogisticRegression

# # Create a classifier object and train on training data
# logistic = LogisticRegression().fit(flights_train)

# # Create predictions for the testing data and show confusion matrix
# prediction = logistic.transform(flights_test)
# prediction.groupBy('label', 'prediction').count().show()

# from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator

# # Calculate precision and recall
# precision = TP / (TP + FP)
# recall = TP / (TP + FN)
# print('precision = {:.2f}\nrecall    = {:.2f}'.format(precision, recall))

# # Find weighted precision
# multi_evaluator = MulticlassClassificationEvaluator()
# weighted_precision = multi_evaluator.evaluate(prediction, {multi_evaluator.metricName: "weightedPrecision"})

# # Find AUC
# binary_evaluator = BinaryClassificationEvaluator()
# auc = binary_evaluator.evaluate(prediction, {binary_evaluator.metricName: "areaUnderROC"})

from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Create a regression object and train on training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Create predictions for the testing data and take a look at the predictions
predictions = regression.transform(flights_test)
predictions.select('duration', 'prediction').show(5, False)

# Calculate the RMSE
RegressionEvaluator(labelCol='duration').evaluate(predictions)

# Intercept (average minutes on ground)
inter = regression.intercept
print(inter)

# Coefficients
coefs = regression.coefficients
print(coefs)

# Average minutes per km
minutes_per_km = regression.coefficients[0]
print(minutes_per_km)

# Average speed in km per hour
avg_speed = 60 / minutes_per_km
print(avg_speed)

from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Create a regression object and train on training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Create predictions for the testing data
predictions = regression.transform(flights_test)

# Calculate the RMSE on testing data
RegressionEvaluator(labelCol='duration').evaluate(predictions)

# Average speed in km per hour
avg_speed_hour = 60 / regression.coefficients[0]
print(avg_speed_hour)

# Average minutes on ground at OGG
inter = regression.intercept
print(inter)

# Average minutes on ground at JFK
avg_ground_jfk = regression.intercept + regression.coefficients[3]
print(avg_ground_jfk)

# Average minutes on ground at LGA
avg_ground_lga = regression.intercept + regression.coefficients[4]
print(avg_ground_lga)

spark.stop()