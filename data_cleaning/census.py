import pandas as pd
df1 = pd.read_csv('us_census_all_oppo_atlas.csv')
df2 = pd.read_csv('TRACT_ZIP_122017.csv')
tract = df2['tract'].values.tolist()
zip = df2['zip'].values.tolist()

geoid = df1['GEO.id2'].values.tolist()
popu_ratio_white = df1['popu_ratio_white'].values.tolist()
popu_ratio_black = df1['popu_ratio_black'].values.tolist()
popu_ratio_asian = df1['popu_ratio_asian'].values.tolist()
mid_age = df1['mid_age'].values.tolist()
jail = df1['jail_pooled_pooled_p25'].values.tolist()
bachelorplus = df1['bachelorplus'].values.tolist()
highschool = df1['highschool'].values.tolist()
employ = df1['employ'].values.tolist()
hh_ratio_married = df1['hh_ratio_married'].values.tolist()
meanic_fam = df1['meanic_fam'].values.tolist()

zipcode = []
ca_popu_ratio_white = []
ca_popu_ratio_black = []
ca_popu_ratio_asian = []
ca_mid_age = []
ca_jail = []
ca_bachelorplus = []
ca_highschool = []
ca_employ = []
ca_hh_ratio_married = []
ca_meanic_fam = []

tozip = {}
for i in range(len(tract)):
    tozip[str(tract[i])] = zip[i]
for i in range(len(geoid)):
    if str(geoid[i])[:2] == '60':
        if str(geoid[i])in tozip.keys():
            zipcode.append(int(tozip[str(geoid[i])]))
            ca_popu_ratio_white.append(float(popu_ratio_white[i]))
            ca_popu_ratio_black.append(float(popu_ratio_black[i]))
            ca_popu_ratio_asian.append(float(popu_ratio_asian[i]))
            ca_mid_age.append(float(mid_age[i]))
            ca_jail.append(float(jail[i]))
            ca_bachelorplus.append(float(bachelorplus[i]/100))
            ca_highschool.append(float(highschool[i]/100))
            ca_employ.append(float(employ[i])/100)
            ca_hh_ratio_married.append(float(hh_ratio_married[i]))
            ca_meanic_fam.append(float(meanic_fam[i]))

df = pd.DataFrame({
    'zipcode':zipcode,
    'popu_ratio_white':ca_popu_ratio_white,
    'popu_ratio_black':ca_popu_ratio_black,
    'popu_ratio_asian':ca_popu_ratio_asian,
    'mid_age':ca_mid_age,
    'jail':ca_jail,
    'bachelorplus':ca_bachelorplus,
    'highschool':ca_highschool,
    'employ':ca_employ,
    'hh_ratio_married':ca_hh_ratio_married,
    'meanic_fam':ca_meanic_fam
}).groupby(by = 'zipcode',as_index=False).mean()

df_result = pd.DataFrame({
    'zipcode':df['zipcode'],
    'popu_ratio_white':[round(i,2)for i in df['popu_ratio_white'].values.tolist()],
    'popu_ratio_black':[round(i,2)for i in df['popu_ratio_black'].values.tolist()],
    'popu_ratio_asian':[round(i,2)for i in df['popu_ratio_asian'].values.tolist()],
    'mid_age':[round(i,2)for i in df['mid_age'].values.tolist()],
    'jail':[round(i,2)for i in df['jail'].values.tolist()],
    'bachelorplus':[round(i,2)for i in df['bachelorplus'].values.tolist()],
    'highschool':[round(i,2)for i in df['highschool'].values.tolist()],
    'employ':[round(i,2)for i in df['employ'].values.tolist()],
    'hh_ratio_married':[round(i,2)for i in df['hh_ratio_married'].values.tolist()],
    'meanic_fam':[round(i,2)for i in df['meanic_fam'].values.tolist()]
})
df_result.to_csv("ca_census.csv", index=False, sep=',',encoding='utf-8')