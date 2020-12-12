from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import geopy

def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    try:
        a = location.raw['address']['postcode']
        return a
    except:
        return '0'

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX : <http://dbpedia.org/resource/>
    PREFIX dbpedia2: <http://dbpedia.org/property/>
    PREFIX dbpedia: <http://dbpedia.org/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?name ?x ?y WHERE {
      ?person dbo:deathPlace ?place.
      ?place geo:lat ?x.
      ?place geo:long ?y.
      FILTER(?x>32.53 and ?x <42.7 and ?y<-122.0667 and ?y>-126.0667 )
      ?person foaf:name ?name .
} ORDER BY ?name
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
i = 0
a = []
b = []
name = []
for result in results["results"]["bindings"]:
    i += 1
    k = result['name']['value'].strip().strip('(').strip(')'.strip('* '))
    if len(name) > 0:
        if len(k) > 0:
            if k != name[-1]:
                name.append(k)
                a.append(float(result['x']['value']))
                b.append(float(result['y']['value']))
    else:
        name.append(k)
        a.append(float(result['x']['value']))
        b.append(float(result['y']['value']))
print(i)
print(len(name))
print(name[-10:-1])
print(len(b))
temp = set(list(zip(a,b)))
print(len(temp))

list1 = []
list2 = []
for item in temp:
    list1.append(item[0])
    list2.append(item[1])
geolocator = geopy.Nominatim(user_agent='myGeocoder')
df = pd.DataFrame({
    'Lat':list1,
    'Lon':list2
})

zipcodes = df.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field='Lat', lon_field='Lon')
zip = zipcodes.values.tolist()
dicresult = {}
for i in range(len(list1)):
    dicresult[(list1[i],list2[i])]= zip[i]

zip = []
for i in range(len(name)):
    zip.append(dicresult[(a[i],b[i])])

df = pd.DataFrame({
    'celebrity':name,
    'zipcode':zip
})
df.to_csv("deathPlace_5.csv", index=False, sep=',',encoding='utf-8')
