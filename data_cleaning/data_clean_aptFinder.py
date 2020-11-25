import jsonlines
import re

def isDigit(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False

data = []
#file_path = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/allcities_aptFinder.jl"
#file_path = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/aptFinder_los_angeles.jl"
#file_path = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_bakerfield.jl"
file_path = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_ventura.jl"

with open(file_path, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        item.pop('id')
        data.append(item)
#test_data = data[1:11]

for i in data:

    if i['title'] != "":
        i['title'] = i['title'].lower()
    else:
        i['title'] = None
    if i['location'] != "":
        if isDigit(i['location'][-5:]):
            i['zipcode'] = i['location'][-5:]
            i['location'] = i['location'].lower()[0:-5].strip()
        else:
            i['location'] = i['location'].lower()
    else:
        i['location'] = None
    if i['price_range'] != "" and i['price_range'].lower() != 'call for rent':
        i['price_range'] = i['price_range'].replace('$','').replace(',','').split(' ')
        if len(i['price_range']) > 1 and '-' in i['price_range']:
            #print('yes',i['price_range'])
            if isDigit(i['price_range'][0]):
                #print('ok',i['price_range'][0]) #ok 1245
                i['lowest_price'] = i['price_range'][0]
            else: i['lowest_price'] = None
            if isDigit(i['price_range'][-1]):
                i['highest_price'] = i['price_range'][-1]
                #print('no',i['highest_price']) #no 945
            else: i['highest_price'] = None
        else:
            if isDigit(i['price_range'][0]):
                i['lowest_price'] = i['price_range'][0]
            else: i['lowest_price'] = None
            i['highest_price'] = None

    elif i['price_range'] == "":
        i['lowest_price'] = None
        i['highest_price'] = None
    else:
        i['lowest_price'] = 'call for rent'
        i['highest_price'] = 'call for rent'
    #print(i['lowest_price'],i['highest_price'],'\n')

    if i['application_fee'] != '':
        i['application_fee'] = i['application_fee'].replace('$','')
    else:
        i['application_fee'] != None

    temp_dict = {}
    if i['pet_policy'] == "Pets Negotiable" or i['pet_policy'] == "":
        temp_dict['cat'] = None
        temp_dict['dog'] = None
        i['pet_policy'] = temp_dict
    else:
        i['pet_policy'] = i['pet_policy'].lower().split()
        if 'cats' in i['pet_policy'] and 'allowed' in i['pet_policy']:
            temp_dict['cat'] = True
        else:
            temp_dict['cat'] = False
        if 'dogs' in i['pet_policy'] and 'allowed' in i['pet_policy']:
            temp_dict['dog'] = True
        else:
            temp_dict['dog'] = False
        i['pet_policy'] = temp_dict

    if i['cat_rent'] != "":
        i['cat_rent'] = i['cat_rent'].replace('$','')
    else:
        i['cat_rent'] = None

    if i['dog_rent'] != "":
        i['dog_rent'] = i['dog_rent'].replace('$','')
    else:
        i['dog_rent'] = None

    if i['cat_deposit'] != "":
        i['cat_deposit'] = i['cat_deposit'].replace('$','')
    else:
        i['cat_deposit'] = None

    if i['dog_deposit'] != "":
        i['dog_deposit'] = i['dog_deposit'].replace('$','')
    else:
        i['dog_deposit'] = None

    if i['assigned_garage_parking_price'] != "":
        i['assigned_garage_parking_price'] = i['assigned_garage_parking_price'].replace('$','').split()
    else:
        i['assigned_garage_parking_price'] = None


    if i['assigned_other_parking_price'] != "":
        i['assigned_other_parking_price'] = i['assigned_other_parking_price'].replace('$','').split()
    else:
        i['assigned_other_parking_price'] = None


    if i['lease_term'] != "":
        #print(i['lease_term'])

        res = re.split(',| |-', i['lease_term'])
        #print("res",res)
        tmp_list = []
        for word in res:
            if isDigit(word):
                tmp_list.append(word)
            else:pass
        #print(tmp_list)

        if len(tmp_list) > 1:
            #print("yes")
            if isDigit(tmp_list[0]):
                i['shortest_lease_term'] = tmp_list[0]
            else:
                i['shortest_lease_term'] = None
            if isDigit(tmp_list[-1]):
                i['longest_lease_term'] = tmp_list[-1]
            else:
                i['longest_lease_term'] = None
            #print("short",i['shortest_lease_term'])
            #print("long",i['longest_lease_term'])
        elif len(tmp_list) == 1:
            if isDigit(tmp_list[0]):
                i['shortest_lease_term'] = tmp_list[0]
                #print("short2", i['shortest_lease_term'])
            else:
                i['shortest_lease_term'] = None
                i['longest_lease_term'] = None
        else:
            i['longest_lease_term'] = None
            i['shortest_lease_term'] = None

    else:
        i['longest_lease_term'] = None
        i['shortest_lease_term'] = None

    i.pop('price_range')
    i.pop('beds')
    i.pop('bath')
    i.pop('lease_term')
    i.pop('parking')

#writer =  jsonlines.open('clean_aptFinder.jl', mode='w')
#writer =  jsonlines.open('clean_aptFinder_la.jl', mode='w')
#writer =  jsonlines.open('clean_aptFinder_bakerfield.jl', mode='w')
writer =  jsonlines.open('clean_aptFinder_ventura.jl', mode='w')
for item in data:
    writer.write(item)



# pop useless attribute last

#print(test_data)