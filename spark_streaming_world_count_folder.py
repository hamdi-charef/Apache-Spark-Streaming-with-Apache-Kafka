
from pyspark.streaming import StreamingContext
from uuid import uuid4
from pyspark import SparkContext

inputDir = './data/'
outputDir = './output/'

sc = SparkContext(appName="spark_streaming_world_coun_folder")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 2)

def saveRDD(rdd):
	if not rdd.isEmpty():
		rdd.saveAsTextFile(outputDir + uuid4().hex)

lines = ssc.textFileStream(inputDir)

counts = lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b)

counts.pprint()

counts.foreachRDD(saveRDD)

# Start the app
ssc.start()

# Wait a few seconds for the app to get started
ssc.awaitTermination()