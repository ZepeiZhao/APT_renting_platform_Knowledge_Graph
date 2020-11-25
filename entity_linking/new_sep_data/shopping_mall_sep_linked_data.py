import jsonlines
import csv
import pandas as pd

file_path = ["/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_bakersfield.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_fairfield.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_fresno.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_la.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_modesto.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_napa.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_oakland.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_redwood-city.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_riverside.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_sacramento.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_san-bernardino.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_san-diego.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_san-francisco.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_san-jose.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_san-rafael.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_santa-ana.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_santa-barbara.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_santa-cruz.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_santa-rosa.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_stockton.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_ventura.jl",
             "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_visalia.jl"]

res = []
for path in file_path:
    with open(path, "r+", encoding="utf8") as f:
        for item in jsonlines.Reader(f):
            data = {}
            data['aptFinder_url'] = item['aptFinder_url']
            data['shopping_mall'] = item['shopping_mall']
            res.append(data)
print(res[6])

new_data_list = []
for i in res:
    if i['shopping_mall']:
        key_list = list(i['shopping_mall'].keys())
        for j in key_list:
            new_dict = {}
            new_dict['aptFinder_url'] = i['aptFinder_url']
            new_dict['shopping_mall'] = j
            if i['shopping_mall'][j]['drive']:
                new_dict['drive'] = float(i['shopping_mall'][j]['drive'].split(" ")[0])
            else:
                new_dict['drive'] = None
            if i['shopping_mall'][j]['distance']:
                new_dict['distance'] = float(i['shopping_mall'][j]['distance'].split(" ")[0])
            else:
                new_dict['distance'] = None
            new_data_list.append((new_dict))
print(new_data_list)

out_file = "shopping_mall.csv"
with open(out_file, 'w') as f:
    w = csv.writer(f)
    fieldnames = list(new_data_list[0].keys())
    w.writerow(fieldnames)
    for row in new_data_list:
        w.writerow(row.values())

final_out_file = "shopping_mall.csv"
path = out_file
data = pd.read_csv(path)
data.duplicated()
data.drop_duplicates()
data.to_csv(final_out_file,index=False)