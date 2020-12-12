import pandas as pd
df1 = pd.read_csv('hometown.csv')
celebrity = [item.strip() for item in df1['celebrity'].values.tolist()]
zipcode = [int(i.split('-')[0]) for i in df1['zipcode'].values.tolist()]
df = pd.DataFrame({
    'zipcode':zipcode,
    'celebrity':celebrity,
})
# df = pd.DataFrame({
#     'zipcode':df1['zipcode'],
#     'celebrity':df1['celebrity'],
# })
df.to_csv("hometown2.csv", index=False, sep=',',encoding='utf-8')