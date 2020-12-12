import pandas as pd
df1 = pd.read_csv('latimes-county-totals.csv')[:58]
df2 = pd.read_csv('ZIP-COUNTY-FIPS_2017-06.csv')
data2 = df2.loc[(df2['STATE']=='CA')&(df2['COUNTYNAME']=='Los Angeles County')]
zipcode = data2['ZIP'].values.tolist()
fp =[i%1000 for i in data2['STCOUNTYFP'].values.tolist()]
dic = {}
fip = df1['fips'].values.tolist()
confirmed_cases = df1['confirmed_cases'].values.tolist()
deaths = df1['deaths'].values.tolist()
for i in range(len(fip)):
    dic[fip[i]] = (confirmed_cases[i],deaths[i])
confirmed = []
death = []
for i in range(len(fp)):
    confirmed.append(dic[fp[i]][0])
    death.append(dic[fp[i]][1])

df = pd.DataFrame({
    'zipcode':zipcode,
    'confirmed_cases':confirmed,
    'deaths':death
})
df.to_csv("la_covid.csv", index=False, sep=',',encoding='utf-8')