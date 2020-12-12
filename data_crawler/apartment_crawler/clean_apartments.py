import json
import os
filePath = './apartment_data'
rootlist = os.listdir(filePath)
for root in rootlist:
    inputpath = './apartment_data'+'/'+root
    outputpath = './cleaned_apartments/cleaned_'+root
    with open(inputpath, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            js = json.loads(line)
            dic = {}
            # url
            dic['url'] = js['url']
            # name
            dic['name'] = js['name']
            # address
            dic['address'] = js['address']
            # zip code
            dic['zipcode'] = js['zipcode']
            # contact
            if len(js['contact'])>0:
                if type(js['contact']) == str:
                    dic['contact'] = js['contact']
                elif type(js['contact']) == list:
                    dic['contact'] = js['contact'][0]
            else:
                dic['contact'] = ''
            # floor plan
            dic['floor plan'] = {}
            if len(js['choice'])>0:
                for item in js['choice']:
                    if item[0] == 'Studio':
                        beds = '0'
                    else:
                        beds = item[0].split()[0]
                    if item[1]:
                        baths_str = item[1].split()[0]
                    else:
                        baths_str = '0'
                    if '½'in baths_str:
                        baths = str(float(baths_str.split('½')[0])+0.5)
                    else:
                        baths = baths_str
                    if not item[2] or item[2] == 'Call for Rent':
                        price = 0
                    else:
                        price = int(item[2].replace( ',',"").split()[0].replace('$',''))
                    sqft = int(item[3].replace(',', "").split()[0])
                    if 'Not'in item[4]:
                        available = False
                    else:
                        available = True
                    itemdic = {}
                    itemdic['lowprice'] = price
                    itemdic['sqft'] = sqft
                    itemdic['available'] = available
                    dic['floor plan'][beds+','+baths] = itemdic
            # parking
            if len(js['parking']) > 0:
                dic['parking'] = True
            else:
                dic['parking'] = False
            # reviews
            if len(js['reviews'])!=0:
                dic['reviews'] = int(js['reviews'].split()[0])
            else:
                dic['reviews'] = 0
            # rating
            if len(js['rating'])!=0:
                temp = js['rating'].split()
                if len(temp) == 3:
                    dic['rating'] = float(temp[0])
                else:
                    dic['rating'] = 0.0
            else:
                dic['rating'] = 0.0
            # nearby schools
            dic['nearby schools'] = {}
            if len(js['nearby schools'])>0:
                for item in js['nearby schools']:
                    school_name = item[0]
                    school_type = item[1]
                    school_contact = item[2]
                    schooldic = {}
                    schooldic['type'] = school_type
                    schooldic['contact'] = school_contact
                    dic['nearby schools'][school_name] = schooldic
            # built in time
            dic['built in time'] = 0
            for item in js['property information']:
                if 'Built'in item:
                    dic['built in time'] = int(item.split()[-1])

            with open(outputpath, mode='a', encoding='utf-8') as f2:
                json_record = json.dumps(dic, ensure_ascii=False)
                f2.write(json_record + '\n')
