
dief-clone:
	mkdir -p target
	git clone https://github.com/Maximiliantoepfer/extraction-framework target/dief

# java 8 required
dief-install:
	cd target/dief; \
	mvn clean install -DskipTests; \
	cd server; \
	mvn package -DskipTests; \

build-docker:
	docker build -t 127.0.0.1:5000/dbpedia/dief .;


test-dief-curl:
	curl -H "Content-Type: application/xml" "localhost:9500/server/extraction/en/extract?format=n-triples" --data @Leipzig
