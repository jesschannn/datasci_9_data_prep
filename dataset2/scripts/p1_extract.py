import pandas as pd 

datalink = 'https://health.data.ny.gov/resource/es3k-2aus.csv'

df = pd.read_csv(datalink)
df.size
df.sample(5)

df.to_pickle('student_weight.pkl')