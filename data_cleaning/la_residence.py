import pandas as pd
df1 = pd.read_csv('residence2.csv')
df2 = pd.read_csv('./result/la_covid.csv')['zipcode'].values.tolist()
df = df1.loc[df1['zipcode'].isin(df2)]
df.to_csv("la_residence.csv", index=False, sep=',',encoding='utf-8')


