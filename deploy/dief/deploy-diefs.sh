IMAGE="vehnem/dbpedia-dief" #"127.0.0.1:5000/dbpedia/dief:latest"

START_PORT=59001
END_PORT=59004

echo "STARTING ALL..."


for PORT in $(seq $START_PORT $END_PORT); do
  docker run -d \
    --name dief_${PORT} \
    -p ${PORT}:9999 \
    ${IMAGE}
  echo "localhost:$PORT"
done

echo "DONE"
