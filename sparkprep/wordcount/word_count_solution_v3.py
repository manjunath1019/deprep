from pyspark.sql import SparkSession
from collections import defaultdict

def process_FASTA_record(iterator):
    hashmap = defaultdict(int)
    for fasta_record in iterator:
        if (fasta_record.startswith(">")):
            hashmap["z"] += 1
        else:
            chars = fasta_record.lower()
            for c in chars:
                hashmap[c] += 1
    return [(k,v) for k,v in hashmap.items()]

def reducefuntionmethod(x,y):
    return x+y

if __name__ == '__main__':
    inputFileName ="wordsinput.fasta"
    appName = "DNA count solution _3"
    runEnv = "local[3]"

    spark = (SparkSession
             .builder
             .master(runEnv)
             .appName(appName)
             .getOrCreate()
             )

    v2filerdd = (
        spark
        .sparkContext
        .textFile(inputFileName)
        .repartition(10)
        .mapPartitions(process_FASTA_record)
        .reduceByKey(reducefuntionmethod)
    )

    #v2filerdd.foreachPartition(lambda x  : print(list(x)))

    print(v2filerdd.collect())