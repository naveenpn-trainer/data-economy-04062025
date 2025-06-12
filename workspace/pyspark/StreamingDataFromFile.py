from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").config("spark.sql.shuffle.partitions",
                                                                                        10).getOrCreate()

    CRIME_SCHEMA = StructType([
        StructField("code", StringType()),
        StructField("location", StringType()),
        StructField("category", StringType()),
    ])
    inputDF = spark.readStream.load(path="./dataset/crime_data/input",
                                    format="CSV",
                                    schema=CRIME_SCHEMA)

    resultDF = inputDF.groupBy(col("location")).count()
    resultDF.writeStream.start(format="console",
                               outputMode="update").awaitTermination()
