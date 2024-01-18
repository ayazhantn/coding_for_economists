#first look at dictionaries

#a dictionary is a collection of key-value pairs.

#syntax:
myDict = {
  "Dog":"Barks",
  "Cat":"Meows",
  "Whale":"Shreeks"
}

print(myDict)

#We cannot use the same indexing syntac as with lists/str
#print(myDict[0]) produced an error

#We can use the key to access the value
print(myDict["Dog"])

#retrieve items of dictionary
print(myDict.items())

#we can also use the len() function
print(len(myDict))