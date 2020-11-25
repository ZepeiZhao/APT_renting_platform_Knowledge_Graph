import jsonlines
import csv
import pandas as pd

file_path = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_la.jl"
# "pet_policy": {"cat": false, "dog": true}
res = []

with open(file_path, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        data = {}
        data['aptFinder_url'] = item['aptFinder_url']
        data['pet_policy'] = item['pet_policy']
        data['cat_deposit'] = item['cat_deposit']
        data['dog_deposit'] = item['dog_deposit']
        data['cat_rent'] = item['cat_rent']
        data['dog_rent'] = item['dog_rent']
        res.append(data)
print(res[6])

new_data_list = []
for i in res:
    if i['pet_policy']:

        new_dict = {}
        new_dict['aptFinder_url'] = i['aptFinder_url']
        new_dict['cat_policy'] = i['pet_policy']['cat']
        new_dict['dog_policy'] = i['pet_policy']['dog']
        new_dict['cat_deposit'] = i['cat_deposit']
        new_dict['dog_deposit'] = i['dog_deposit']
        new_dict['cat_rent'] = i['cat_rent']
        new_dict['dog_rent'] = i['dog_rent']

        new_data_list.append((new_dict))
print(new_data_list)

out_file = "la_pet.csv"
with open(out_file, 'w') as f:
    w = csv.writer(f)
    fieldnames = list(new_data_list[0].keys())
    w.writerow(fieldnames)
    for row in new_data_list:
        w.writerow(row.values())

final_out_file = "la_pet.csv"
path = out_file
data = pd.read_csv(path)
data.duplicated()
data.drop_duplicates()
data.to_csv(final_out_file,index=False)