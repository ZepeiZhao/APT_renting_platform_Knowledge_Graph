# add zillow
# aptFinder, zillow
import jsonlines
import rltk
import re

def title_similarity(string1, string2):
    res = rltk.levenshtein_similarity(string1, string2)
    return res

def location_similarity(string1, string2):
    res = rltk.levenshtein_similarity(string1, string2)
    return res

def zipcode_similarity(string1, string2):
    res = rltk.levenshtein_similarity(string1, string2)
    return res

def weight_sim(string1,string2,string3,string4):
    res = 0.9*location_similarity(string1,string2) + 0.1*title_similarity(string3,string4)
    return res

file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/apartments_los-angele.jl"
file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_la.jl"
file_zillow = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/zillow_LA.jl"
apartments_list = []
with open(file_apartments, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        apartments_list.append(item)
print(apartments_list[0])

aptFinder_list = []
with open(file_aptFinder, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        aptFinder_list.append(item)
print(aptFinder_list[0])

zillow_list = []
with open(file_zillow, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        zillow_list.append(item)
print(zillow_list[0])

dict_pair_z_af = {}
list_pair_z_af = []
for i in aptFinder_list:
    tmp_dict_z_af = {}
    tmp_pair_list = []
    for j in zillow_list:
        weight_zillow_aptFinder = location_similarity(i['location'].lower(),j['address'].lower())
        if weight_zillow_aptFinder > 0.8:
            tmp_dict_z_af[j['link']] = weight_zillow_aptFinder
        else:pass
    if len(tmp_dict_z_af)>1:
        new_dict_list = sorted(tmp_dict_z_af.items(), key=lambda d: d[1], reverse=True)
        tmp_res = list(new_dict_list[0])
        dict_pair_z_af[i['url']] = tmp_res[0]
        # tmp_pair_list.append(dict_pair_z_af[i['url']])
        # tmp_pair_list.append(tmp_res[0])
        # list_pair_z_af.append(tmp_pair_list)

    elif len(tmp_dict_z_af)>0:
        key = list(tmp_dict_z_af)[0]
        dict_pair_z_af[i['url']] = key
        # tmp_pair_list.append(dict_pair_z_af[i['url']])
        # tmp_pair_list.append(key)
        # list_pair_z_af.append((tmp_pair_list))
    else: pass
print(dict_pair_z_af)
# print("res",list_pair_z_af)
