# -> [[url1,url2],...]
# aptFinder + apartment

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
    res = 0.7*location_similarity(string1,string2) + 0.3*title_similarity(string3,string4)
    return res

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_los-angele.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_la.jl"
# file_zillow = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/zillow_LA.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_bakersfield.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_bakerfield.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_fairfield.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_fairfield.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_fresno.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_fresno.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_modesto.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_modesto.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_napa.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_napa.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_oakland.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_oakland.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_redwood-city.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_redwood_city.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_riverside.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_riverside.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_sacramento.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_sacramento.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_san-bernardino.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_san_bernardino.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_san-diego.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_san_diego.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_san-francisco.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_san_francisco.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_san-jose.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_san_jose.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_san-rafael.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_san_rafael.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_santa-ana.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_santa_ana.jl"

file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_santa-barbara.jl"
file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_santa_barbara.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_santa-cruz.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_santa_cruz.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_santa-rosa.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_santa_rosa.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_stockton.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_stockton.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_ventura.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_ventura.jl"

# file_apartments = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/cleaned_apts/cleaned_apartments_visalia.jl"
# file_aptFinder = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/clean_aptFinder_visalia.jl"




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

# zillow_list = []
# with open(file_zillow, "r+", encoding="utf8") as f:
#     for item in jsonlines.Reader(f):
#         zillow_list.append(item)
# print(zillow_list[0])

pair_list = []
dictFor = {}
for i in aptFinder_list:
    aptFinder_zipcode = i['zipcode']
    tmp_dict = {}
    tmp_pair_list = []
    for j in apartments_list:
        if j['zipcode'] == aptFinder_zipcode:
            weight = weight_sim(i['location'].replace(' ','').lower(),j['address'].lower(),i['title'].lower(),j['name'].lower())
            if weight > 0.2:
                tmp_dict[j['url']] = weight
            else:pass
        else:pass

    #student_1_sort = sorted(student_1.iteritems(), key=lambda d: d[1], reverse=True)
    if len(tmp_dict)>1:
        new_dict_list = sorted(tmp_dict.items(),key=lambda d:d[1],reverse=True)
        tmp_res = list(new_dict_list[0])
        dictFor[i['url']] = tmp_res[0]
        # tmp_pair_list.append(dictFor[i['url']])
        # tmp_pair_list.append(tmp_res[0])
        # pair_list.append(tmp_pair_list)
    else:
        if len(tmp_dict) > 0:
            key = list(tmp_dict)[0]
            dictFor[i['url']] = key
            # tmp_pair_list.append(dictFor[i['url']])
            # tmp_pair_list.append(key)
            # pair_list.append(tmp_pair_list)
        else:pass

print(dictFor)
print(len(dictFor))
# print("res",pair_list)

cnt = 0

res = []
for key,value in dictFor.items():
    for j in aptFinder_list:
        for h in apartments_list:
            res_dict = {}
            if key == j['url'] and value == h['url']:
                res_dict['aptFinder_url'] = j['url']
                res_dict['apts_url'] = h['url']
                res_dict['title'] = j['title']
                res_dict['location'] = h['address']
                res_dict['zipcode'] = j['zipcode']
                res_dict['lowest_price'] = j['lowest_price']
                res_dict['highest_price'] = j['highest_price']
                res_dict['floor_plan'] = h['floor plan']
                res_dict['phone'] = h['contact']
                res_dict['description'] = j['apartment_description']
                res_dict['pet_policy'] = j['pet_policy']
                res_dict['cat_rent'] = j['cat_rent']
                res_dict['dog_rent'] = j['dog_rent']
                res_dict['cat_deposit'] = j['cat_deposit']
                res_dict['dog_deposit'] = j['dog_deposit']
                res_dict['parking'] = h['parking']
                #res_dict['property_information'] = h['property information']
                res_dict['floorplan_amenities'] = j['floorplan_amenities']
                res_dict['community_features'] = j['community_features']
                res_dict['reviews'] = h['reviews']
                res_dict['rating'] = h['rating']
                res_dict['nearby_schools'] = h['nearby schools']
                res_dict['universities'] = j['universities']
                res_dict['transit'] = j['transit']
                res_dict['commuter_rail'] = j['commuter_rail']
                res_dict['shopping_mall'] = j['shopping_mall']
                res_dict['park_recreation'] = j['park_recreation']
                res_dict['military_bases'] = j['military_bases']
                res_dict['airport'] = j['airport']
                res_dict['built_in_time'] = h['built in time']
                res_dict['rent_special'] = j['rent_special']
                if 'longest_lease_term' in j.keys():
                    res_dict['longest_lease_term'] = j['longest_lease_term']
                else:
                    res_dict['longest_lease_term'] = None
                res_dict['shortest_lease_term'] = j['shortest_lease_term']
                res_dict['office_hour'] = j['office_hour']
                res.append(res_dict)
            else:pass
print("cnt",cnt)
# print(res_dict)

#writer = jsonlines.open('./link_data/link_la.jl', mode='w')
# writer = jsonlines.open('./link_data/link_bakersfield.jl', mode='w')
# writer = jsonlines.open('./link_data/link_fairfield.jl', mode='w')
# writer = jsonlines.open('./link_data/link_fresno.jl', mode='w')
# writer = jsonlines.open('./link_data/link_modesto.jl', mode='w')
# writer = jsonlines.open('./link_data/link_napa.jl', mode='w')
# writer = jsonlines.open('./link_data/link_oakland.jl', mode='w')
# writer = jsonlines.open('./link_data/link_redwood-city.jl', mode='w')
# writer = jsonlines.open('./link_data/link_riverside.jl', mode='w')
# writer = jsonlines.open('./link_data/link_sacramento.jl', mode='w')
# writer = jsonlines.open('./link_data/link_san-bernardino.jl', mode='w')
# writer = jsonlines.open('./link_data/link_san-diego.jl', mode='w')
# writer = jsonlines.open('./link_data/link_san-francisco.jl', mode='w')
# writer = jsonlines.open('./link_data/link_san-jose.jl', mode='w')
# writer = jsonlines.open('./link_data/link_san-rafael.jl', mode='w')
# writer = jsonlines.open('./link_data/link_santa-ana.jl', mode='w')
writer = jsonlines.open('./link_data/link_santa-barbara.jl', mode='w')
# writer = jsonlines.open('./link_data/link_santa-cruz.jl', mode='w')
# writer = jsonlines.open('./link_data/link_santa-rosa.jl', mode='w')
# writer = jsonlines.open('./link_data/link_stockton.jl', mode='w')
# writer = jsonlines.open('./link_data/link_ventura.jl', mode='w')
# writer = jsonlines.open('./link_data/link_visalia.jl', mode='w')



for item in res:
    writer.write(item)