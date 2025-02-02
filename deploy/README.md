# Infrastructure Deployment

Explains the deployment of the spark and dief services on a docker swarm cluster.

### Spark

First set your environmet variables at spark/env.env
```bash
cd spark;
docker stack -f docker-compose.yml
```

### DBpedia extraction framework

Building the DIEF docker image
```
cd dief
make dief-prepare
make dief-install
make docker-build
```

Deploy DIEF cluster

**OPTION 1** Use dedicated services
```
cd dief
deploy-dief.sh $STARTPORT $ENDPORT $NDOE1 $NODE2 ...
```

**OPTION 2** Use ingress or other balancing
```
cd dief
docker service create -n dief -p 9999:9999 --replicas $SCALE 127.0.0.1:5000/dbpedia/dief
```



