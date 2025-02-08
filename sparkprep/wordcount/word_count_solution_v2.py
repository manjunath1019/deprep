from pyspark.sql import SparkSession
from collections import defaultdict
def process_FASTA_record(fasta_record):
    if (fasta_record.startswith(">")):
        return [("z", 1)]
    hashmap = defaultdict(int)
    chars = fasta_record.lower()
    for c in chars:
        hashmap[c] = hashmap[c]+1
    return [(k,v) for k,v in hashmap.items()]

def reducefuntionmethod(x,y):
    return x+y

if __name__ == '__main__':
    inputFileName ="wordsinput.fasta"
    appName = "DNA count solution _2"
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
        .flatMap(process_FASTA_record)
        .reduceByKey(reducefuntionmethod)
    )

    print(v2filerdd.collect())