from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()

    #  Input Table
    inputDf = spark.readStream.load(format="socket",
                                    host="localhost",
                                    port="9999")

    #  Incremental Query

    # Write the data
    inputDf.writeStream.start(format="console", outputMode="append" ).awaitTermination()
