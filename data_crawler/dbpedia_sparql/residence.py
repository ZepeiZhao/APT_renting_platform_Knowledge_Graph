import json
import pandas as pd

with open("./sparql_rawdata/sparql_residence.json","r",encoding='utf-8') as f:
    new_dict = json.loads(f.read())

    dic = new_dict['results']['bindings']
    celebrity = []
    residence = []
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
                if (name == celebrity[-1]):
                    pass
                else:
                    celebrity.append(name)
                    residence.append(place)
                    lat.append(float(x))
                    long.append(float(y))
            else:
                celebrity.append(name)
                residence.append(place)
                lat.append(float(x))
                long.append(float(y))
    dataframe = pd.DataFrame({'celebrity': celebrity,'residence':residence,'x':lat,'y':long})
    dataframe.to_csv("residence_raw.csv", index=False, sep=',',encoding='utf-8')