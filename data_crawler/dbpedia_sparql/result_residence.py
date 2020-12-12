import pandas as pd

df1 = pd.read_csv('residence.csv')
celebrity = df1['celebrity'].values.tolist()
x = df1['x'].values.tolist()
y = df1['y'].values.tolist()
points = list(zip(x,y))


df2 = pd.read_csv('zip_code residence.csv')
Lat = df2['Lat'].values.tolist()
Lon = df2['Lon'].values.tolist()
zipcode = df2['zipcode'].values.tolist()
dic = {}
temp = list(zip(Lat,Lon))
for i in range(len(temp)):
    dic[temp[i]]= zipcode[i]

zip = []
for item in points:
    if item in dic.keys():
        zip.append(dic[item])
    else:
        zip.append('0')

df = pd.DataFrame({
    'celebrity':celebrity,
    'zipcode':zip
})
df.to_csv("Residence.csv", index=False, sep=',',encoding='utf-8')