#number of times each country won a tender in the ted-sample.csv file

#task 1: find index position of the column "WIN_COUNTRY_CODE"
# grab the headers and assign them to a variable. Iterate through the headers and print the index position of the column "WIN_COUNTRY_CODE" using enumerate()

#find headers/idxs for relevant vars: ISO_COUNTRY_CODE, WIN_COUNTRY_CODE
f = open('data/raw/european_commission/ted-sample.csv', 'r') #the second argument is the mode. 'r' is for reading

#grab headers
headers = f.readline().strip().split(',')
#strip is for getting rid of spaces, leaves only actual numbers or letters

#split is for splitting the string into a list

#make sure to close the file
f.close()

for index, value in enumerate(headers):
  print(index, value)

# WIN_COUNTRY_CODE at index 61
  
#task 2: instantiate an empty list called data

data=[]
  
#task 3: iterate through the rows (each line) of the csv file using the context manager open() and append the observation as a list. Hint: Use the .split() method on the line to automatically create a list, passing the appropriate argument to split().

  #3.1 iterate through each row in ted-sample.csv and
  #3.2 append each row to the data list using (in the loop body) 

with open('data/raw/european_commission/ted-sample.csv') as f: 
  for line in f:
    data.append(list(line.split(",")))

#print(data[0])
#print(data[1])

#output should look like data = [[row1], [row2], [row3], ...]]
  
# 4. count the number of wins by country

d={}

#get rid of row 0 which is the headers
data.pop(0)
#or data=data[1:]

for row in data:
  country=row[61] #careful: some tenders are won by more than one country
  countries = country.split('---') #returns a list of winning countries
  for winning_country in countries:
    if not winning_country in d:
        d[winning_country] = 0
    d[winning_country] += 1
print (d)
#output should look like:
# d = {'country1': N1, 'country2': N2, ...}, ..., 'countryN': NN}
  
#hint: 'a, b, c'.split(",")=['a', 'b', 'c']