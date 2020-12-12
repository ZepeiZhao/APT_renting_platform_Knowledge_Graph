import json
import pandas as pd
import geopy

def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    try:
        a = location.raw['address']['postcode']
        return a
    except:
        return 0

with open("./sparql_rawdata/sparql_hometown.json","r",encoding='utf-8') as f:
    new_dict = json.loads(f.read())

    dic = new_dict['results']['bindings']
    celebrity = []
    hometown = []
    lat = []
    long = []
    for item in dic:
        name_temp = item['name']['value']
        name = name_temp.strip().strip('(').strip(')'.strip('* '))
        x = item['x']['value']
        y = item['y']['value']
        temp = item['place']['value']
        place = temp.split('/')[-1].replace("_"," ").split(',')[0]
        if len(name)>0:
            if len(celebrity)>0:
                if (name == celebrity[-1])or name[0]not in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                    pass
                else:
                    celebrity.append(name)
                    hometown.append(place)
                    lat.append(float(x))
                    long.append(float(y))
            else:
                celebrity.append(name)
                hometown.append(place)
                lat.append(float(x))
                long.append(float(y))
    dataframe = pd.DataFrame({'celebrity': celebrity,'hometown':hometown,'x':lat,'y':long})
    # dataframe.to_csv("hometown_raw.csv", index=False, sep=',',encoding='utf-8')

    temp = set(list(zip(lat,long)))
    list1 = []
    list2 = []
    for item in temp:
        list1.append(item[0])
        list2.append(item[1])
    geolocator = geopy.Nominatim(user_agent='myGeocoder')
    df = pd.DataFrame({
        'Lat': list1,
        'Lon': list2
    })

    zipcodes = df.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field='Lat', lon_field='Lon')
    zip = zipcodes.values.tolist()
    dicresult = {}
    for i in range(len(list1)):
        dicresult[(list1[i], list2[i])]: zip[i]
    print(dicresult)
    outputdf = pd.DataFrame({
        'Lat': list1,
        'Lon': list2,
        'zipcode': zip
    })
    outputdf.to_csv("zip_code hometown.csv", index=False, sep=',', encoding='utf-8')