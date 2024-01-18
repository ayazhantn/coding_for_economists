#In this file we will loot at lists, dictionaries, set, tuples, and lambda functions
#List
myList=[1,2,3,4,5]
print(myList)

print(type(myList))

#Grab first object of List
print(myList[0]) #1

#How many objects are in our list?
print(f'Our list object myList has {len(myList)} elements.')

#Nice thing about lists" they are flexible with respect to the data type
mixedList=[1, 'two', 3.0, [4, 'four'], 5] #can store lists in list
print(mixedList)

#we can also add and remove objects from a list
mixedList.append(6)
print(mixedList)

#words followed by () is a function // methods are functions tieds to a specific object

#removing
#mixedList.pop(0) 
#print(mixedList)

#without 0 (index) it will pop the last
mixedList.pop()
print(mixedList)

#how many times does the integer 1 appear?
print(mixedList.count(1))

#Reverse a list
mixedList.reverse()
print(mixedList)