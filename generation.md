# Guidelines To Extract an DBpedia-TKG variant

We separated the process into 3 stages:
1. deployment
2. extraction
3. evaluation

# 1. Infrastructure Deployment

Explains the deployment of the spark and dief services on a docker swarm cluster.
All relevant scripts are located in `./deploy`.

### Spark Cluster (Skip if already deployed)

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

# 2. Extraction

# 3. Evaluation

