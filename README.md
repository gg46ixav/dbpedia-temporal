# DBpedia Temporal Graph Extraction

The DBpedia Temporal Knowledge Graph (DBpedia-TKG) is an extension of the DBpedia framework that incorporates temporal dynamics, capturing the evolution of knowledge from Wikipedia over time. It provides a rich temporal dataset with over 1.7 billion triples and 270 million distinct start and end times for their lifespans, derived from Wikipedia's meta-history dumps. This repository includes detailed configurations, such as temporal filters and DBpedia ontology versions, enabling flexible extractions tailored to specific use cases. With its temporal annotations, DBpedia-TKG supports advanced applications in temporal reasoning, predictive modeling, and performance benchmarking. It is a valuable resource for researchers and developers interested in dynamic knowledge representation and temporal graph analytics. The dataset is openly available under the CC BY-SA 4.0 license.

# Repository Structure

- **[deploy](deploy/)**  contains the relvant files to deploy the DIEF servers and the SPARK cluster to Docker Swarm.
- **[execute](execute)** contains relevant scripts to execute and evaluate DBpedia Temporal construction.
- **[eval](eval)** contains python code to plot the results from the eval process 
- **[ODIBEL]()** framework that currently contains the Scala SPARK code for construction and evaluation of the DBpedia temporal graph (will be migrated soon!)

# Datasets 

<p float="left">
  <img src="eval/figures/snapshot_evolution.png" width="49%" />
  <img src="eval/figures/degree_distribution.png" width="49%" /> 
</p>

| Name | Varian | Version | DOI | Other Links |
| --- | --- | --- | --- | ---|
| DBpedia-TKG | FULL | 2024-06-01 | [10.5281/zenodo.14532571](https://doi.org/10.5281/zenodo.14532571) | [Other Formats \& Supplements](https://cloud.scadsai.uni-leipzig.de/index.php/s/QeyqwaWSqPgpHdq) |

# Data Model

CSV Snippet
```
```

NQ Snippet
```
```

# Development 

Development notes.

## Pull Submodule

```
git submodule update --init --recursive
```

# Licence

The Generator is `GPLv3` and the Dataset is `CC-BY-SA 4.0.`
