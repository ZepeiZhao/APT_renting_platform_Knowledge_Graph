import pandas as pd
celebrity = []
zipcode = []
dic = {}

df1 = pd.read_csv('./data/residence.csv',encoding='GBK')
a = df1['celebrity'].values.tolist()
b = df1['zipcode'].values.tolist()
for i in range(len(a)):
    if a[i][0] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] and b[i]!='0':
        dic[a[i]] = b[i]
print(len(dic.keys()))
for key in dic.keys():
    celebrity.append(key)
    zipcode.append(dic[key])

df = pd.DataFrame({
    'celebrity':celebrity,
    'zipcode':zipcode
})
df.to_csv("./data/residence2.csv", index=False, sep=',',encoding='utf-8')