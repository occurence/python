from pyspark import SparkContext

sc = SparkContext()

# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)