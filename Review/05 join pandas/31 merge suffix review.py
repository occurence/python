import pandas as pd

grants = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\grants.csv')
wards = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\ward.p')
biz_owners = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\business_owners.p')
licenses = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\licenses.p')

# print(licenses.head(3))
licenses = licenses.dropna()
licenses['zip'] = licenses['zip'].astype(int)
# print(licenses.isna().sum())
# grants['zip'] = grants['zip'].astype(int)
# print(wards.info())
# print(grants.info())
print(wards.dtypes)
print(licenses.dtypes)
# print(grants.merge(licenses, on=['address', 'zip']))
# print(licenses)
# print(wards)

print(grants.merge(licenses, on=['address', 'zip']).merge(wards, on='ward', suffixes=('_bus', '_ward')))