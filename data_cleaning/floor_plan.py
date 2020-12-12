import pandas as pd
df1 = pd.read_csv('new_linked_data.csv')
apts_url = df1['apts_url'].values.tolist()
floor_plan = df1['floor_plan'].values.tolist()
result_apts_url = []
result_beds = []
result_baths = []
result_sqft = []
result_price = []
temp = eval(floor_plan[0])
for i in range(len(apts_url)):
    if len(floor_plan[i])>0:
        temp = eval(floor_plan[i])
        if len(temp.keys())>0:
            for key in temp.keys():
                if temp[key]['available'] == True:
                    result_apts_url.append(apts_url[i])
                    result_beds.append(float(key.split(',')[0]))
                    k = key.split(',')[1]
                    if '¼'in k:
                        t = k.replace('¼','')
                    else:
                        t = k
                    result_baths.append(float(t))
                    result_sqft.append(float(temp[key]['sqft']))
                    result_price.append(float(temp[key]['lowprice']))

df = pd.DataFrame({
    'apts_url':result_apts_url,
    'beds':result_beds,
    'baths':result_baths,
    'sqft':result_sqft,
    'price':result_price
})
df.to_csv("floor_plan.csv", index=False, sep=',',encoding='utf-8')