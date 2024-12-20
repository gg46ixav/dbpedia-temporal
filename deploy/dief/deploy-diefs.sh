IMAGE="127.0.0.1:5000/dbpedia/dief:latest"

START_PORT=59017
END_PORT=59032

NODES=("athena2" "athena3" "athena4" "athena5" "athena6" "athena7" "athena8" "athena9")

echo "STARTING ALL..."

for NODE in "${NODES[@]}"; do
  for PORT in $(seq $START_PORT $END_PORT); do
    docker service create \
      --name service_${NODE}_${PORT} \
      --constraint "node.hostname == ${NODE}" \
      --replicas 1 \
      --publish published=${PORT},target=9999,mode=host \
      ${IMAGE}
    echo "$NODE:$PORT"
  done
done

echo "DONE"
