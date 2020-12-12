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

dictFor = {}
for i in aptFinder_list:
    aptFinder_zipcode = i['zipcode']
    tmp_list = []
    for j in apartments_list:
        tmp_dict = {}
        large = 0
        if j['zipcode'] == aptFinder_zipcode:
            weight = weight_sim(i['location'].lower(),j['address'].lower(),i['title'].lower(),j['name'].lower())
            tmp_dict[j['url']] = weight
            if weight > 0.8:
                tmp_list.append(tmp_dict)
            else:pass

        else:pass

        # {url1:[{url2:w1]}
    dictFor[i['url']] = tmp_list
    cnt = 0
    if tmp_list == []:
        cnt+=1
    else:pass
print("cnt null link", cnt)

print(dictFor)


print(len(dictFor))