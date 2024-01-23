#let's have a look at loop syntax

#for loop operate on "iterables"

#let's create an iterable object
myList = [1, 2, 'abc']

#let's interate over the object
for banana in myList:
  #loop body needs to be indented once
  if banana ==1:
    print(banana)
  else:
    print("item not equal to 1.")

#looping over a range of values
print("Using range(5)")
for i in range(5): #range() generates value on the fly -- here from 0 to 4 -- has memory advantages // widely used generator
  print(i)

#another way to do it
range_vals=[0, 1, 2, 3, 4] #not memory efficient
print("Using a list to display values 0-4")
for i in range_vals:
  print(i)

#looping over list of strings and nesting loops
for name in ['Alice', 'Bob', 'Charlie']:
  print(name) #prints a name
  for letter in name:
    print(letter) #prints each letter as a new line

#using the enumerate() function to get both index and value
print("Using enumerate()")
for index, name in enumerate(['Alice', 'Bob', 'Charlie']):
  print(index, name)

#equiaveltn loop using indexing
myList=['Alice', 'Bob', 'Charlie']
for index in range(len(myList)):
  print(index, myList[index])

#use a loop to create a list of capital letters from A-Z
print("Using a loop to create a list of capital letters from A-Z")
alphabet=[]
for i in range (65, 91):
  #print(i, chr(i)) #prints each letter as a new line and with its decimal unicode in front of it
  alphabet.append(chr(i))

#alternatively
#for i in range (0, 26):
  #alphabet.append(chr(65+i))

print(alphabet)

# while loops
# while loops are used when you do not know how many times you want to loop
i=0
while i<10: #while True #will be infinite
  print(i)
  #increment our counter every iteration
  i+=1 #prints 10 numbers from 0 to 9

#list comprehensions

#let's have a look at a for loop creating a list of squares from 0 to 10
squares=[]
for num in range(0,11):
  squares.append(num**2)
print(squares)

#doing the same using list comprehension -- one line for loop
#always in square brackets
squares=[num**2 for num in range(0,11)]
print(squares)

#using if statements in list comprehensions to get squares of only even numbers
even_squares=[num**2 for num in range(0,11) if num%2==0]
print(even_squares)