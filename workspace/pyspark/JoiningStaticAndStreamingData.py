from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()

    customerDF = spark.read.csv(path="./dataset/customer_transaction/customers/",
                                header=True)


    TranscationSchema = StructType([
        StructField("id",IntegerType()),
        StructField("amount", IntegerType()),
        StructField("CustomerID", IntegerType()),
    ])

    transactionDF =  spark.readStream.load(path="./dataset/customer_transaction/transactions/input",
                                    format="CSV",
                                    schema=TranscationSchema)

    resultDF = transactionDF.join(customerDF,"CustomerID","inner").select("CustomerID","Gender","amount")

    resultDF.writeStream.start(format="console",
                               outputMode="append").awaitTermination()



