
distribution gif: 
- Page rank distribution across nodes. 
- The red line shows the threshold at which nodes get merged
- the more iterations (step in gif) the higher the page rank for the nodes

---
high_prob_scaler_[...]

- "high_prob_scaler"  means that there was a higher probability of nodes being connected within their cluster 
- shows networks of nodes with different number of communities (2 vs. 5) 
- raw = the network itself with each color being their TRUE community
- Louvain = the network how the Louvain clustering algorithm sees it with the color being the INFERRED community

---
legalBases_bySector
- legal bases as defined in Art. 6(1) by ILO sector (https://ilostat.ilo.org/resources/concepts-and-definitions/classification-economic-activities/)


---
legalBases_ITvsRest
- legal bases as defined in Art 6(1) grouped by IC (category J) and non-IC (all other)
- shows that IC has general interest 6(1)(f) disproportionally higher than others

---
low_prob_scaler
- same as high_prob_scaler but with low probability of nodes being connected in their cluster (i.e. less underlying clustering for the algorithm to detect) 
-> Compare high vs. low prob scaler to show that the underlying strength of connectivity between nodes is important for Louvain (or other unsupervised algorithms) to detect the communities 

---
No_categories_per_controller

- number of categories in data disclosed section per individual controller

---
no_communities_detected_vs_probability_of_connection

- the relationship between Louvain communities detected and probability of nodes being connected within same cluster (i.e. increased intra-cluster-connectivity)
- -> Louvain in this simulation case not very successful at narrowing down to the correct number of communities even though the graph becomes more separated into clusters. 
- there should be 5 communities detected

---
no_purposes_per_controller

- number of purposes as purposes in data disclosed per controller
- binomial distribution makes sense as each additional purpose is less likely 

---
node density per community

- kernel density of nodes in inferred communities. 
- Each line is a different prob_scaler (how dense is the underlying graph)


---
node_count_by_pageRankThreshold:
- sobald page-rank > threshold, merge with other node
- wir sehen die kurven für vertschiede thresholds
- pro Schritt: random sample of node, quasi-random merge (mit höherer wahrscheinlichkeit zu merge im gleichen cluster)



---
sorensen_threshold: 
- je höher similarity, desto eher werden die Verbindungen geknüpft
