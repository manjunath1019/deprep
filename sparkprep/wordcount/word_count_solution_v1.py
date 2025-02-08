from pyspark.sql import SparkSession

def process_FASTA_record(fasta_record):
    key_value_list = []
    #print(fasta_record)
    if (fasta_record.startswith(">")):
        key_value_list.append(("z", 1))
    else:
        chars = fasta_record.lower()
        #print("chars=", chars)
        for c in chars:
            key_value_list.append((str(c), 1))
    #print(key_value_list)
    return key_value_list

if __name__ == '__main__':
    inputFileName ="wordsinput.fasta"
    appName = "DNA count solution _1"
    runEnv = "local[3]"

    spark = (SparkSession
             .builder
             .master(runEnv)
             .appName(appName)
             .getOrCreate()
             )

    filerddv1 = (spark
               .sparkContext
               .textFile(inputFileName)
               .flatMap(process_FASTA_record)
               .groupByKey()
               .mapValues(lambda s : sum(s))
               )
    print(filerddv1.collect())

    filerddv2 = (
        spark
        .sparkContext
        .textFile(inputFileName)
        .flatMap(process_FASTA_record)
        .reduceByKey(lambda x,y : x+y)
    )
    print(filerddv2.collect())
    spark.stop()
