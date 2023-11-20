import pandas as pd 

datalink = 'https://data.cityofnewyork.us/api/views/5uac-w243/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)

df.to_pickle('nypd.pkl')