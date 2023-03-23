# TAP: A Platform for Cross-Provider Analysis of Transparency Information

Transparency and accountability are indispensable principles for modern data protection, from both, the legal and technical viewpoints. Regulations such as the GDPR therefore require specific transparency information to be provided including, e.g., purpose specifications, storage periods, or legal bases for personal data processing. However, it has repeatedly been shown that all too often, this information is practically hidden in legalese privacy policies, hindering data subjects from exercising their rights. This paper presents a novel approach to enable large-scale transparency information analysis across service providers, leveraging machine-readable formats and graph data science methods. More specifically, we propose a transparency analysis platform (TAP) that is used to empirically identify data transfers, provide evidence-based analyses of sharing-clusters of more than 70 real-world data controllers, or even to simulate network dynamics using synthetic transparency information for large-scale data-sharing scenarios. We provide a general approach for advanced transparency information analysis, an open source architecture and implementation in the form of a queryable analysis platform, and versatile analysis examples. These contributions pave the way for more transparent data processing for data subjects, and evidence-based enforcement processes for data protection authorities. Future work can build upon our contributions to gain more insights in so-far hidden data-sharing practices.


## Setup



If you have docker installed and running, you should be able to start your instance using: 
```
docker compose build --no-cache
```
```
docker compose up
```

Afterwards, you can also access the instance through [neo4j Desktop](https://neo4j.com/download/).  

## Content

There are two Jupyter Notebooks [tilt_to_neo.ipynb](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/tilt_to_neo4j.ipynb) and [synthetic data](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/synthetic_data.ipynb) that allow an analysis of tilt data using neo4j. 

The jupyter notebooks should be run top to bottom but especially the analysis cells can be modified and used for ones own analysis of the data. 

###  [tilt_to_neo.ipynb](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/tilt_to_neo4j.ipynb) 

This file's purpose is to convert the tilt database from its json format into a graph database hosted on Neo4J. It converts the JSON files into a GraphQL query that is send to Neo4J through the GraphQL API which is part of the GRANDStack. For the query to be executed, all components of the tilt need to be according to the [schema](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/api/src/schema.graphql). The schema is based on the json tilt schema but allows for some extra flexibilities regarding the formatting of the content. 

Note that when uploading the tilts into neo4j, duplicates will be created. For debugging purposes one may want to run 
```
match (m) detach delete m
```
in the neo4j browser instance to delete all nodes and relationships in the graph.


### [synthetic_data](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/synthetic_data.ipynb)

The file builds a data base of a synthetic tilt possessing a subsample of the structure of a full tilt graph. A number of analysis such as clustering and dynamic simulation are implemented. The synthetic data is generated using names of the Fortune 500 and can be hyperparamterized on a number of dimensions. 

To use multiple neo4j instances at the same time, a neo4j Enterprise license is needed. To run the data science algorithms implemented in neo4j, the Graph Data Science (GDS) package and the apoc package should also be installed. 

Using neo4j Bloom (launch from neo4j Desktop) GDS algorithms and visualisations can be used. The dynamic simulation class contains a GIF method that allows for the generation of GIFs out of graph plots that have been generated using networkX. 

### [visuals](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/visuals)

All graphs/gifs/neo4j-Bloom visualisations have been placed in the visuals folder. 
