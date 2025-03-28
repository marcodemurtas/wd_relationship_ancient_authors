# wd_relationship_ancient_authors

This script reads the authority record of an author (in this case Aristotle) ​​from a database (in this case VIAF) and by communicating with Wikidata extracts the bibliographic records linked to it on Wikidata itself. The work is done in three phases:

1) reading authority ID on native database;

2) queries the Wikidata dataset with a SPARQL query to find the corresponding author and his bibliographic links;

3) prints the bibliographic works linked to the author directly or indirectly (first author or other elements of bibliographic description);

Requirements: Python 3.x.x

How to use it: python bib_auth.py

ENJOY !
