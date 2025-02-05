# Guidelines To Extract an DBpedia-TKG variant

We separated the generation process into 3 stages:
1. deployment
2. extraction
3. evaluation

> `However`, while the full deployment requires good understanding of Docker SWARM, SPARK and HDFS we first provide a basic setup, that will utelize a single DIEF docker container, the local FS, and runs without SPARK.

# Quickly Running without SPARK

Requirements for Linux:
> git, docker, wget, java 8 & 17, maven, p7zip, make

Preparing single DIEF container and building Generator Code
```bash
# checkout repository and build components
git clone --recurse-submodules https://github.com/dbpedia/dbpedia-temporal

# build generator code
cd dbpedia-temporal/ODIBEL
mvn package

# start dief container exposing port 9999
docker run -d -p 9999:9999 --name dbpedia-dief vehnem/dbpedia-dief 
```
This will take some time to start everything, check http://localhost:9999/server/extraction/en for health

Downloading a compressed wikimedia meta-history dump file (~170MB)
```bash
# Tries to download one of the latest meta-history dump files in the 7z format
URL=https://dumps.wikimedia.org/enwiki/latest/; curl -s "$URL" | grep -P "meta-history1.*7z" | head -1 | grep -Po '"\Kenwiki[^"]+' | while read -r fname; do echo "$URL$fname"; wget "$URL$fname" -O meta-history.xml.7z; done
```
if this fails go to https://dumps.wikimedia.org/enwiki/latest/ and download it manually


Run a simple extraction on the downloaded files first 1M rows
```bash
7z e -so meta-history.xml.7z | head -1000000 | \
java -cp target/*dependencies.jar ai.scads.odibel.main.Main dbpedia-tkg extract \
-i - -o - -f csv -e http://localhost:9999/server/extraction/en
```

Use `-f ngraph` to output the ngraph format (using sort -u might be required to remove duplicated start:tkg and tkg:end meta quads if multiple triples share the same lifespan).

# Running with SWARM, HDFS, SPARK

- [ ] TODO add statisitics on hardware requirements and usage

## 1. Infrastructure Deployment

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

## 2. Extraction

# 3. Evaluation

The `generation` contains scripts for calculating statistics or metrics, and ploting results.

