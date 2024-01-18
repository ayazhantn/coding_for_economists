#intro to data type set

#set is a collection of well defined objects (unordered items)
mySet={1,2,3}
print(mySet)

#Check type
print(type(mySet))

#set only contains unique values
mySet={1,2,3,3} #duplicate 3 gets removed
print(mySet)

#check membership
print(1 in mySet)

print(set('aaaaaabbbbbbbbccc'))

#define two sets and check out set operations
setA={1,2,3}
listB=[3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]
setB=set(listB)

print(setA, setB)

#set union
unionAB=setA | setB
print(unionAB)

#intersection
intersecAB=setA&setB
print(intersecAB)