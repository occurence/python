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

# Apply the hashing trick and transform to TF-IDF
hasher = HashingTF(inputCol='terms', outputCol="hash")
idf = IDF(inputCol='hash', outputCol="features")

# Create a logistic regression object and add everything to a pipeline
logistic = LogisticRegression()
pipeline = Pipeline(stages=[tokenizer, remover, hasher, idf, logistic])



sms_train, sms_test = sms.randomSplit([0.8, 0.2], seed=13)
pipeline = pipeline.fit(sms_train)
prediction = pipeline.transform(sms_test)

# Create a confusion matrix, comparing predictions to known labels
prediction.groupBy('label', 'prediction').count().show()
prediction.select('label', 'prediction', 'probability').show(5, False)


spark.stop()