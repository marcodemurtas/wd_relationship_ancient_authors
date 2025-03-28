import requests
from SPARQLWrapper import SPARQLWrapper, JSON

def sparql_query(query):
    endpoint_url = "https://query.wikidata.org/sparql"
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    results = sparql.query().convert()
    return results["results"]["bindings"]

def get_viaf_data(viaf_id):
    url = f"http://viaf.org/viaf/{viaf_id}.xml"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def find_books_by_viaf(viaf_id):
    query = f"""
    SELECT ?book ?bookLabel
    WHERE {{
        ?author wdt:P214 "{viaf_id}".
        ?book wdt:P50 ?author.
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    """
    return sparql_query(query)

viaf_id_aristotle = "7524651"  

books_from_viaf = find_books_by_viaf(viaf_id_aristotle)

print("Records found for Aristotle on Wikidata (via VIAF):")
for result in books_from_viaf:
    print(f"Title (or wikidata ID): {result['bookLabel']['value']}")

#In case needed also VIAF records
#viaf_data = get_viaf_data(viaf_id_aristotle)
#if viaf_data:
#    print("\nAristotle's VIAF records:")
#   print(viaf_data) 


