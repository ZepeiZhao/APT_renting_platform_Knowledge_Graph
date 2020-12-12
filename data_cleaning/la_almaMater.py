import pandas as pd
celebrity = []
almaMater = []

df1 = pd.read_csv('almaMaterLA.csv')
a = df1['celebrity'].values.tolist()
b = df1['almaMater'].values.tolist()
for i in range(len(a)):
    if a[i][0] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] and b[i]!='0':
        celebrity.append(a[i])
        almaMater.append(b[i])
print(len(celebrity))
df = pd.DataFrame({
    'celebrity':celebrity,
    'almaMater':almaMater
})
df.to_csv("la_almaMater.csv", index=False, sep=',',encoding='utf-8')