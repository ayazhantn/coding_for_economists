# introduction to pandas and numpy
# pandas is a python library for data manipulation
import pandas as pd
import numpy as np

# let's look at pd.Series
# a series is a 1-dimensional array-like object

#let's define our first pd.Series

#documentation:
#https://pandas.pydata.org/docs/reference/api/pandas.Series.html

ps = pd.Series([1, 'a', 2, np.pi])
print(ps)

#which data type does out pd.Series have?
print(type(ps))

#we can access the values
print(ps.values)

#data type of the values stored - array
a = ps.values
print(type(a))

#access elements of pd.Series by indexing
print(ps[0:2])

#define a custom index
series_1 = pd.Series(
  data = ["Schnitzel",
         "Lemonade",
         "Whiskey"],
  index = ["Food",
          "Soda",
          "Alcohol"]
)

#advanced indexing of pd.Series
#using .loc[]
print(series_1.loc["Food"])

#accessing more than a single index
print(series_1.loc[["Food", "Alcohol"]])

#using .iloc[]
print(series_1.iloc[0])

#access elements from a range of indexes
print(series_1.loc["Food": "Alcohol"])
print(series_1.iloc[0:2])