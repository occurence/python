import pandas as pd

licenses = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\licenses.p')
zip_demo = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\zip_demo.p')
wards = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\ward.p')

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))