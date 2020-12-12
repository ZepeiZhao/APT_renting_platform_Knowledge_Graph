import json
import pandas as pd

with open("./sparql_rawdata/sparql_almaMater.json","r",encoding='utf-8') as f:
    new_dict = json.loads(f.read())

    dic = new_dict['results']['bindings']
    celebrity = []
    almaMater = []
    for item in dic:
        name_temp = item['name']['value']
        name = name_temp.strip().strip('(').strip(')')
        x = item['x']['value']
        y = item['y']['value']
        temp = item['place']['value']
        school = temp.split('/')[-1].split(',')[0].replace("_"," ")
        if len(name)>0:
            if len(celebrity)>0:
                if name == celebrity[-1] and school == almaMater[-1]:
                    pass
                else:
                    celebrity.append(name)
                    almaMater.append(school)
            else:
                celebrity.append(name)
                almaMater.append(school)
    dataframe = pd.DataFrame({'celebrity': celebrity, 'almaMater': almaMater})
    dataframe.to_csv("almaMater.csv", index=False, sep=',')
