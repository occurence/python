from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline


spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()

# Read data from CSV file
sms = spark.read.csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\24_Course_Machine_Learning_with_PySpark\datasets\sms.csv',
                         sep=';',
                         header=False,
                         inferSchema=True,
                         nullValue='NA')

sms = sms.toDF('id', 'text', 'label')

sms.show(5)

# Break text into tokens at non-word characters
tokenizer = Tokenizer(inputCol='text', outputCol='words')

# Remove stop words
remover = StopWordsRemover(inputCol='words', outputCol='terms')

# # Apply the hashing trick and transform to TF-IDF
hasher = HashingTF(inputCol='terms', outputCol="hash")
idf = IDF(inputCol='hash', outputCol="features")

# # Create a logistic regression object and add everything to a pipeline
logistic = LogisticRegression()
pipeline = Pipeline(stages=[tokenizer, remover, hasher, idf, logistic])



# sms_train, sms_test = sms.randomSplit([0.8, 0.2], seed=13)
# pipeline = pipeline.fit(sms_train)
# prediction = pipeline.transform(sms_test)

# # Create a confusion matrix, comparing predictions to known labels
# prediction.groupBy('label', 'prediction').count().show()
# prediction.select('label', 'prediction', 'probability').show(5, False)

from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# Create parameter grid
params = ParamGridBuilder()

# Add grid for hashing trick parameters
params = params.addGrid(hasher.numFeatures, [1024, 4096, 16384]) \
               .addGrid(hasher.binary, [True, False])

# Add grid for logistic regression parameters
params = params.addGrid(logistic.regParam, [0.01, 0.1, 1.0, 10.0]) \
               .addGrid(logistic.elasticNetParam, [0.0, 0.5, 1.0])

# Build parameter grid
params = params.build()
print('Number of models to be tested: ', len(params))

from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol='label', predictionCol='prediction', metricName='accuracy')

# Create cross-validator
cv = CrossValidator(estimator=pipeline, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)
sms_train, sms_test = sms.randomSplit([0.8, 0.2], seed=13)
cv = cv.fit(sms_train)

# Get the best model from cross validation
best_model = cv.bestModel

# Look at the stages in the best model
print(best_model.transform(sms_test))

# Get the parameters for the LinearRegression object in the best model
print(best_model.stages)
print(best_model.stages[4].extractParamMap())

# Generate predictions on testing data using the best model then calculate RMSE
predictions = best_model.transform(sms_test)
predictions.select('label', 'prediction', 'probability').show(5, truncate=False)
print("Accuracy =", evaluator.evaluate(predictions))
spark.stop()