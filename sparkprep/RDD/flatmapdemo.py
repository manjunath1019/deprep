from pyspark.sql import SparkSession

def creatpair(t):
    return t

def scan(t):
    print(list(t))

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Flat Map Demo").master("local[3]").getOrCreate()

    list_of_arrays = [
        ['item_11', 'item_12', 'item_13'],
        ['item_21', 'item_22'],
        [],
        ['item_31', 'item_32', 'item_33', 'item_34'],
        []
        ]

    rdd=spark.sparkContext.parallelize(list_of_arrays).repartition(3)
    print(rdd.foreachPartition(scan))
    rdd2 = rdd.flatMap(creatpair)
    print(rdd2.collect())

    rdd2.foreachPartition(lambda x  : print(list(x)))


    numbers = [1,2,3,4,5]
    rdd3 = spark.sparkContext.parallelize(numbers)
    rdd4 = rdd3.flatMap(lambda x : range(1,x))
    print("---",rdd4.collect())

    rdd5 = rdd3.flatMap(lambda v : ((v,v+5),(v+5,v)))
    print(rdd5.collect())