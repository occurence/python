from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print(spark)

# Print the tables in the catalog
print(spark.catalog.listTables())