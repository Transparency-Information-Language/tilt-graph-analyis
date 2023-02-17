# Analysing the TILT Hub with Graph Data Science

## Start

This project is based on the GRANDstack Starter. To begin using it clone this repo and follow the instructions below and create the neo4j instance using [Docker](https://docs.docker.com/get-docker/). 
The UI component of the app is deprecated and does not work. It can be ignored.

You should be able to start your instance using: 
```
docker compose build --no-cache
```
```
docker compose up
```

Afterwards you can also access the instance through [neo4j Desktop](https://neo4j.com/download/).  

## Content

There are two Jupyter Notebooks [tilt_to_neo.ipynb](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/tilt_to_neo4j.ipynb) and [fake_data](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/fake_data.ipynb) that allow an analysis of tilt data using neo4j. 

The jupyter notebooks should be run top to bottom but especially the analysis cells can be modified and used for ones own analysis of the data. 

###  [tilt_to_neo.ipynb](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/tilt_to_neo4j.ipynb) 

This file's purpose is to convert the tilt database from its json format into a graph database hosted on Neo4J. It converts the JSON files into a GraphQL query that is send to Neo4J through the GraphQL API which is part of the GRANDStack. For the query to be executed, all components of the tilt need to be according to the [schema](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/api/src/schema.graphql). The schema is based on the json tilt schema but allows for some extra flexibilities regarding the formatting of the content. 

Note that when uploading the tilts into neo4j, duplicates will be created. For debugging purposes one may want to run 
```
match (m) detach delete m
```
in the neo4j browser instance to delete all nodes and relationships in the graph.


### [fake_data](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/fake_data.ipynb)

The file builds a data base of a fake tilt possessing a subsample of the structure of a full tilt graph. A number of analysis such as clustering and dynamic simulation are implemented. The fake data is generated using names of the Fortune 500 and can be hyperparamterized on a number of dimensions. 

To use multiple neo4j instances at the same time, a neo4j Enterprise license is needed. To run the data science algorithms implemented in neo4j, the Graph Data Science (GDS) package and the apoc package should also be installed. 

Using neo4j Bloom (launch from neo4j Desktop) GDS algorithms and visualisations can be used. The dynamic simulation class contains a GIF method that allows for the generation of GIFs out of graph plots that have been generated using networkX. 

### [visuals](https://github.com/Transparency-Information-Language/tilt-graph-analyis/blob/main/visuals)

All graphs/gifs/neo4j-Bloom visualisations have been placed in the visuals folder. 