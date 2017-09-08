# Apache-Spark-Streaming-with-Apache-Kafka
Apache Kafka is a distributed publish-subscribe messaging while other side Spark Streaming brings Spark's language-integrated API to stream processing, allows to write streaming applications very quickly and easily.<br />
<br />
It supports Python, Java and Scala.<br />
<br />
In this tutorial we are going to explore Apache Kafka, Zookeeper and Spark with streaming example using Spark Streaming.<br />

__Prerequisites__

	- Python
	- Apache Spark
	- Apache Kafka
	- Apache Apache ZooKeeper

### Approach 1: Receiver-based Approach:

This approach uses a Receiver to receive the data. The Receiver is implemented using the Kafka high-level consumer API. As with all receivers, the data received from Kafka through a Receiver is stored in Spark executors, and then jobs launched by Spark Streaming processes the data.
This approach can lose data under failures. To ensure zero-data loss, i have to additionally enable Write Ahead Logs in Spark Streaming. This synchronously saves all the received Kafka data into write ahead logs on a distributed file system (e.g HDFS), so that all the data can be recovered on failure.<br />
In the streaming application code, import KafkaUtils and create an input DStream as follows.<br />

__Programming:__

Code example in the file “1_approach_spark_kafka.py”<br />

__Deploying and running:__

For Python applications, spark-streaming-kafka-0-8_2.11 and its dependencies can be directly added to spark-submit using --package<br />

```
./spark-submit --packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.0.0 1_approach_spark_kafka.py localhost:9092 my_topic
```


### Approach 2: Direct Approach (No Receivers):

This is a new approach (introduced in Spark 1.3) without using Receivers. They have different programming models, performance characteristics, and semantics guarantees.<br />

This approach periodically queries Kafka for the latest offsets in each topic+partition, and accordingly defines the offset ranges to process in each batch.<br />
When the jobs to process the data are launched, Kafka’s simple consumer API is used to read the defined ranges of offsets from Kafka.<br />

__Programming:__

Code example in the file “2_approach_spark_kafka.py”<br />

__Deploying and running:__

For Python applications, spark-streaming-kafka-0-8_2.11 and its dependencies can be directly added to spark-submit using --package<br />

```
./spark-submit --packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.0.0 2_approach_spark_kafka.py localhost:9092 my_topic
```


### Apache Spark World count:

In this part i will show how to run a Apache Spark word count application.<br />

	- Creates a SparkContext. A Spark application corresponds to an instance of the SparkContext class. When running a shell, the SparkContext is 
	reated or you.
	- Gets a word frequency threshold.
	- Reads an input set of text documents from the directory passed as an argument.
	- Counts the number of times each word appears.

__Programming:__

Code example in the file “spark_world_count_folder.py”<br />

__Deploying and running:__

For Python applications, we run with spark-submit python file parameters <br />

```
./spark-submit spark_world_count_folder.py ./data/

or we can specify file type 

./spark-submit spark_world_count_folder.py ./data/*.txt

./spark-submit spark_world_count_folder.py ./data/*.csv
```

### Apache Spark Streaming World count:

In this part i will show how to run a Apache Spark Streaming word count application which counts words from files in folder each 2 second batches of streaming data. <br />

	- Creates a StreamingContext and SparkContext. A Spark application corresponds to an instance of the SparkContext class. When running a shell, the SparkContext is 
	reated or you. 
	- Gets a word frequency threshold.
	- Reads an input set of text documents from the directory passed as an argument.
	- Counts the number of times each word appears.
	- Define an output folder where to store results.

Run the program and start adding new files to the data folder.<br />

__Programming:__

Code example in the file “spark_streaming_world_count_folder.py”<br />

__Deploying and running:__

For Python applications, we run with spark-submit python file parameters <br />

```
./spark-submit spark_streaming_world_count_folder.py

```