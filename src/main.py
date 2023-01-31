# src/main.py
from pyspark.sql import SparkSession

def count_words(file_path: str) -> dict:
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    text_file = spark.sparkContext.textFile(file_path)
    word_counts = text_file.flatMap(lambda line: line.split()).countByValue()
    return dict(word_counts)

