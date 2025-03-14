#!/usr/bin/env bash

source env.sh

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

copyJarToSpark() {
    docker cp $SCRIPT_DIR/../ODIBEL/target/odibel-1.0-SNAPSHOT-jar-with-dependencies.jar $MASTER_CONTAINER:/opt/spark/work-dir/job.jar
    docker exec -u root $MASTER_CONTAINER chown spark:spark /opt/spark/work-dir/job.jar
}

execOdibelSpark() {
    docker exec $MASTER_CONTAINER \
    bash -c "HADOOP_USER_NAME=$HADOOP_USER_NAME \
    /opt/spark/bin/spark-submit \
    --name "ODIBEL" \
    --master spark://master:7077 \
    --driver-memory 2g \
    --executor-memory $EXECUTOR_MEMORY \
    --executor-cores $EXECUTOR_CORES \
    $EXECUTOR_OPTS \
    --class ai.scads.odibel.main.Main \
    job.jar $*"
}

propertyEval() {
        docker exec $MASTER_CONTAINER \
    bash -c "HADOOP_USER_NAME=$HADOOP_USER_NAME \
    /opt/spark/bin/spark-submit \
    --name "ODIBEL" \
    --master spark://master:7077 \
    --driver-memory 2g \
    --executor-memory $EXECUTOR_MEMORY \
    --executor-cores $EXECUTOR_CORES \
    $EXECUTOR_OPTS \
    --class ai.scads.odibel.datasets.wikitext.eval.PropertyEval \
    job.jar $*"
}

genSubGraphs() {
    docker exec $master \
    bash -c "HADOOP_USER_NAME=hadena \
    /opt/spark/bin/spark-submit \
    --master spark://athena1:37077 \
    --name "ODIBEL" \
    --driver-memory 2g \
    --executor-memory 256g \
    --executor-cores 64  \
    --conf spark.hadoop.fs.defaultFS=hdfs://athena1.informatik.intern.uni-leipzig.de:9000 \
    --class ai.scads.odibel.main.Main \
    job.jar $*"
}

$*
