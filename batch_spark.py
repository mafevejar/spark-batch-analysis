from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BatchAnalysis").getOrCreate()

df = spark.read.csv("house_mini.csv", header=True, inferSchema=True)

df.show()

df_clean = df.dropna()

df_clean.show()

df_clean.describe().show()

df_clean.filter(df_clean.price > 100000).show()
