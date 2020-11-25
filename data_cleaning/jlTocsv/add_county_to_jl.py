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

# file = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_la.jl"
#
# res = []
# with open(file, "r+", encoding="utf8") as f:
#     for item in jsonlines.Reader(f):
#         item['county'] = 'los angeles'
#         res.append(item)
# print(res[2])
print(len(file_path))
county = ['bakersfield','fairfield','fresno','los angeles','modesto','napa','oakland','redwood-city','riverside','sacramento',
          'san-bernardino','san-diego','san-francisco','san-jose','san-rafael','santa-ana','santa-barbara','santa-cruz','santa-rosa','stockton','ventura','visalia']
print(len(county))
res = []
for i in range(len(file_path)):
    with open(file_path[i], "r+", encoding="utf8") as f:
        for item in jsonlines.Reader(f):
            item['county'] = county[i]
            res.append(item)



out_file = "sep_data/new_jl_add_county/new_linked_data.csv"
with open(out_file, 'w') as f:
    w = csv.writer(f)
    fieldnames = list(res[0].keys())
    w.writerow(fieldnames)
    for row in res:
        w.writerow(row.values())