from pyspark.sql import SparkSession

def createPair(data):
    name,age= data[0], data[2]
    return (name,age)

if __name__ == '__main__':
    spark = (SparkSession
             .builder
             .master("local[3]")
             .appName("Mapper Demo")
             .getOrCreate()
             )

    tuple_data = [
        ('alex', 'Sunnyvale', 25),
        ('alex', 'Sunnyvale', 33),
        ('mary', 'Ames', 22),
        ('mary', 'Cupertino', 66),
        ('jane', 'Ames', 20),
        ('bob', 'Ames', 26)
    ]
    rdd=spark.sparkContext.parallelize(tuple_data)
    print(rdd.collect())

    rdd1=rdd.map(createPair)
    print(rdd1.collect())

    rdd2 = rdd1.mapValues(lambda v : v+5)
    print(rdd2.collect())

    ## Note :  map can be achived by dataframe by Withcolumn ##
    spark.stop()