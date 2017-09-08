import sys
from pyspark import SparkContext

sc = SparkContext(appName='spark_world_count_files')
sc.setLogLevel("WARN")

distFile = sc.textFile(sys.argv[1])
#distFile = sc.textFile('./input/*.txt')

nonempty_lines = distFile.filter(lambda x: len(x) > 0)

print 'Nonempty lines', nonempty_lines.count()

words = nonempty_lines.flatMap(lambda x: x.split(' '))

wordcounts = words.map(lambda x: (x, 1)) \
                  .reduceByKey(lambda x, y: x+y) \
                  .map(lambda x: (x[1], x[0])).sortByKey(False)

print 'Top 100 words:'
print wordcounts.take(100)