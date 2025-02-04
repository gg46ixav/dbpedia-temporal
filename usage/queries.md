# Example Queries

## SQL

## SPARQL (NQ format)

```
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://example.org/tkg/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?population ?start ?end
WHERE {
  GRAPH ?g {
    dbr:Berlin dbo:populationTotal ?population .
  }
  GRAPH ?tkg {
    ?g tkg:start ?start ;
       tkg:end ?end .
  }
}
LIMIT 10
```

```
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://dbpedia.org/temporal/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?p ?o {
 GRAPH ?g {dbr:Leipzig ?p ?o . } 
 GRAPH ?tkg { 
    ?g tkg:start ?start  ;
         tkg:end ?end  .
         FILTER( ?end >= xsd:dateTime("2024-10-03T02:10:30") && ?start <= xsd:dateTime("2024-10-03T02:10:30") )
   }
}
```

```
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://dbpedia.org/temporal/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?o ?start ?end {
 GRAPH ?g {dbr:Leipzig <http://dbpedia.org/ontology/wikiPageWikiLink> ?o . } 
 GRAPH ?tkg { 
    ?g tkg:start ?start  ;
         tkg:end ?end  .
   }
} ORDER BY ?end
```

```
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX tkg: <http://dbpedia.org/temporal/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT(?p) (COUNT(?start)  as ?c) {
 GRAPH ?g {dbr:Leipzig ?p ?o . } 
 GRAPH ?tkg { 
    ?g tkg:start ?start  ;
         tkg:end ?end  .
   }
} ORDER BY ?c
```