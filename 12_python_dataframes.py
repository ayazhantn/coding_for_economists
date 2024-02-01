# intro to pandas.DataFrames
import pandas as pd
import numpy as np

#create some raw data to construct df
data = {'Tokyo': 30_000_000,
       'Delhi': 50_000_000,
       'Shanghai': 200_000_000}

#create df from dict
df = pd.DataFrame(data=data, index=[0])

print(df)

#create a dataframe from a csv
df_raw = pd.read_csv('https://osf.io/yzntm/download')

#inspect
df_raw.head()

#what are the dimensions of our data?
print(df_raw.shape)


type(df_raw.shape)
# <class 'tuple'>

#access number of rows
print(df_raw.shape[0])

#name of columns
print(df_raw.columns)

#create new column; multiple ways of doing so
# df.nnights = 1
# df['nnights'] = 1
df = df_raw.assign(nnights=1)

#delete df_raw since we do not need it anymore
del df_raw

#let's check out accommodationtype variable
df['accommodationtype'].head()

#we want to clean this up
df['accommodationtype'] = df['accommodationtype'].str.split('@').str[1]

#how many nights in each accommodationtype?
df.accommodationtype.value_counts()

#replace empty string values to unknown // clean up missing value
df.accommodationtype.replace("", "Unknown", inplace=True)

#look at guestreviewrating
df['guestreviewrating''].head()

#create clean variable for ratings
df['ratings']=df['guestreviewsrating']
.str.split('/').str[0].str.strip()
df['ratings'].head()

#convert to floar
df['ratings']=df['ratings'].astype('float')

#what is the average rating?
df['ratings'].mean()

#if you have matplotlib installed then you can
#df.ratings.hist()

#small exercise: there's a varibla ecalled center1distance. what's the average distance to the center?
df_raw['center1distance'].head()
df_raw['center1distance'] = df_raw['center1distance'].str.split(' ').str[0]
df_raw['center1distance']=df_raw['center1distance'].astype('float')
df_raw['center1distance'].mean()

#there are a few ratings-related variables; let's inspect them
print(df.filter(regex='rating').head())

#renaming variables
df = df.rename(columns={'rating_reviewcount': 'rating_count', 'rating2_ta':'ratingta'}, inplace=True)

#rename the following variables
#ratings2_ta_reviewcount: ratingta_count
#addresscountryname: country
#starrating: stars
#s_city: city
df = df.rename(columns={'addresscountryname': 'country', 'starrating': 'stars', 'ratings2_ta_reviewcount': 'ratingta_count', 's_city': 'city'}, inplace=True)
df=pd.read_csv('https://osf.io/yzntm/download')

#subsetting data
#only look at hotels
print(df.loc[df['accommodationtype']=='Hotel'])

#how to check for missing valus
print(df.ratings.isnull().sum())

#how many are missing per country?
print(df.ratings.isnull().groupby(df.country).sum())