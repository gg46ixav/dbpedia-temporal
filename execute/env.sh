MASTER_CONTAINER_PREFIX=spark-master
MASTER_CONTAINER="$(docker ps --format '{{.Names}}' | grep $MASTER_CONTAINER_PREFIX)"
HADOOP_USER_NAME=hadena
EXECUTOR_MEMORY=8g
EXECUTOR_CORES=8
# SUBMIT_OPTS="--conf spark.hadoop.fs.defaultFS=hdfs://athena1.informatik.intern.uni-leipzig.de:9000"

