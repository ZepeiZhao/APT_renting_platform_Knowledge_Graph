import jsonlines
import csv
import pandas as pd

file_path = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_la.jl"
res = []

with open(file_path, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        data = {}
        data['aptFinder_url'] = item['aptFinder_url']
        data['park_recreation'] = item['park_recreation']
        res.append(data)
print(res[6])

new_data_list = []
for i in res:
    if i['park_recreation']:
        key_list = list(i['park_recreation'].keys())
        for j in key_list:
            new_dict = {}
            new_dict['aptFinder_url'] = i['aptFinder_url']
            new_dict['park_recreation'] = j
            if i['park_recreation'][j]['drive']:
                new_dict['drive'] = float(i['park_recreation'][j]['drive'].split(" ")[0])
            else:
                new_dict['drive'] = None
            if i['park_recreation'][j]['distance']:
                new_dict['distance'] = float(i['park_recreation'][j]['distance'].split(" ")[0])
            else:
                new_dict['distance'] = None
            new_data_list.append((new_dict))
print(new_data_list)

out_file = "la_park_recreation.csv"
with open(out_file, 'w') as f:
    w = csv.writer(f)
    fieldnames = list(new_data_list[0].keys())
    w.writerow(fieldnames)
    for row in new_data_list:
        w.writerow(row.values())

final_out_file = "la_park_recreation.csv"
path = out_file
data = pd.read_csv(path)
data.duplicated()
data.drop_duplicates()
data.to_csv(final_out_file,index=False)