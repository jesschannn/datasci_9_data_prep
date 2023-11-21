import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw

datalink = 'https://health.data.ny.gov/resource/es3k-2aus.csv'

df = pd.read_csv(datalink)

## get column names
df.columns

## do some data cleaning of column names, 
## make them all lower case, replmove white spaces and rpelace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

## get data types
df.dtypes 
len(df)

## drop columns
to_drop = [
    'location_code',
    'area_name',
    'region',
    'school_years',
    'overweight_1',
    'overweight_2',
    'obese_2',
    'overweight_or_obese_1',
    'overweight_or_obese_2',
    'number_healthy_weight',
    'percent_healthy_weight'
]
df.drop(to_drop, axis=1, inplace=True, errors='ignore')

## county --> will need to encode this
df.county.value_counts()

## perform orindla encoding on county
enc = OrdinalEncoder()
enc.fit(df[['county']])
df['county'] = enc.transform(df[['county']])

## create dataframe with mapping
df_mapping_county = pd.DataFrame(enc.categories_[0], columns=['county'])
df_mapping_county['county_ordinal'] = df_mapping_county.index
df_mapping_county.head(5)
# save mapping to csv
df_mapping_county.to_csv('mapping_county.csv', index=False)





## obese_1--> will need to encode this
df.obese_1.value_counts()

## perform orindla encoding on obese_1
enc = OrdinalEncoder()
enc.fit(df[['obese_1']])
df['obese_1'] = enc.transform(df[['obese_1']])

## create dataframe with mapping
df_mapping_obese = pd.DataFrame(enc.categories_[0], columns=['obese_1'])
df_mapping_obese['obese_1_ordinal'] = df_mapping_obese.index
df_mapping_obese.head(5)
# save mapping to csv
df_mapping_obese.to_csv('mapping_obese.csv', index=False)





## grade_category --> will need to encode this
df.grade_category.value_counts()

## perform orindla encoding on grade_category
enc = OrdinalEncoder()
enc.fit(df[['grade_category']])
df['grade_category'] = enc.transform(df[['grade_category']])

## create dataframe with mapping
df_mapping_grade = pd.DataFrame(enc.categories_[0], columns=['grade_category'])
df_mapping_grade['grade_category_ordinal'] = df_mapping_grade.index
df_mapping_grade.head(5)
# save mapping to csv
df_mapping_grade.to_csv('mapping_grade.csv', index=False)





## sex
df.sex.value_counts()
## drop row if sex is equal to ALL
df = df[df['sex'] != 'ALL' ]
df.sex.value_counts()
## perform orindla encoding on sex
enc = OrdinalEncoder()
enc.fit(df[['sex']])
df['sex'] = enc.transform(df[['sex']])

## create dataframe with mapping
df_mapping_sex = pd.DataFrame(enc.categories_[0], columns=['sex'])
df_mapping_sex['nsex_ordinal'] = df_mapping_sex.index
df_mapping_sex.head(5)
# save mapping to csv
df_mapping_sex.to_csv('mapping_sex.csv', index=False)

len(df)

#### save temporary csv files to test the model
df.head(600).to_csv('student_weight_600.csv', index=False)
df.sample(500).to_csv('student_weight_500.csv', index=False)
df.sample(400).to_csv('student_weight_400.csv', index=False)