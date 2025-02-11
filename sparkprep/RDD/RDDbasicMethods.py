from pyspark import SparkConf, SparkContext

def printPartionedData(rddpart):
    print(rddpart.glom().collect())

def mapfundemo(element)->int:
    return int(element*10)

def flapdemo(element):
     yield element

def filteredDemo(element):
    if int(element)>20:
        return element

def mappartdemo(iter):
    returnlist = []
    for item in iter:
        returnlist.append(item*10)
    return  returnlist

if __name__ == '__main__':
    conf = SparkConf()
    (conf.setAppName("RDD Basic Demo")
     .setMaster("local[*]"))

    sc = SparkContext(conf=conf)


    import random

    randomList = random.sample(range(1,40),10)
    print(randomList)

    randomListRdd= sc.parallelize(randomList,3)
    randomListRdd.cache()

    # get Number of partitions
    print("Number of paritions :: ", randomListRdd.getNumPartitions())

    print("Display partition wise data")
    print(randomListRdd.glom().collect())

    print("Repartition")
    repartrdd = randomListRdd.repartition(2)
    printPartionedData(repartrdd)

    print(randomListRdd.count())

    print("Mapped data.....")
    map_rdd = randomListRdd.map(mapfundemo)
    printPartionedData(map_rdd)

    print("Faltted data.....")
    flatmap_rdd = randomListRdd.flatMap(flapdemo)
    print(flatmap_rdd.collect())
    printPartionedData(flatmap_rdd)

    print("Filtered data....")
    filteredrdd = randomListRdd.filter(filteredDemo)
    print(randomListRdd.filter(lambda x: x > 20).collect())
    printPartionedData(filteredrdd)

    print("Map parition data.....")

    mappartitionedrdd = randomListRdd.mapPartitions(mappartdemo)
    printPartionedData(mappartitionedrdd)

    randomList2 = random.sample(range(1,20),10)
    randomList2Rdd = sc.parallelize(randomList2,3)

    randomList2Rdd.cache()
    #Union
    print(randomListRdd.collect())
    print(randomList2Rdd.collect())
    unionrdd = randomListRdd.union(randomList2Rdd)
    printPartionedData(unionrdd)

    #intersection
    intersectionrdd = randomListRdd.intersection(randomList2Rdd)
    intersectionrdd=intersectionrdd.coalesce(5)
    printPartionedData(intersectionrdd)

    #fold
    foldedrdd = randomListRdd.fold(0,lambda x,y :x+y)
    print(foldedrdd)


    print(randomListRdd.max(),randomListRdd.min(),randomListRdd.mean(),randomListRdd.stdev(),randomListRdd.sum())