# Example Queries

Some example queries on specific TKG representation models.

## SPARQL (RDF NQ format)

Show temporal information for all property value paris of dbr:Leipzig.

```sparql
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://dbpedia.org/temporal/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?start ?end ?property ?value
WHERE {
  GRAPH ?g {
    dbr:Leipzig ?property ?value .
  }
  GRAPH ?tkg {
    ?g tkg:start ?start ;
       tkg:end ?end .
  }
} ORDER BY ?start
```

---

Get all triples of Leipzig at a specific datetime.

```sparql
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://dbpedia.org/temporal/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?property ?value {
 GRAPH ?g {
      dbr:Leipzig ?property ?value . 
   } 
   GRAPH ?tkg { 
      ?g tkg:start ?start  ;
         tkg:end ?end  .
         FILTER( ?start <= xsd:dateTime("2024-10-03T02:10:30")  && ?end >= xsd:dateTime("2024-10-03T02:10:30") )
   }
}
```

---

Show number of property changes for dbr:Leipzig.

```
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://dbpedia.org/temporal/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT(?property) (COUNT(?start)  as ?changes) {
 GRAPH ?g {dbr:Leipzig ?property ?value . } 
 GRAPH ?tkg { 
    ?g tkg:start ?start  ;
         tkg:end ?end  .
   }
} ORDER BY DESC(?changes)
```

## Notes

LC_ALL=C sort -u  leipzig.tkg.nq  | grep -P '(populationTotal)' | sort -V -k4 -t' '