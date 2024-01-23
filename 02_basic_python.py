#Basic arithmetic operations in Python

#add two numbers
print(2+4)

#divide two numbers
print(10/5)

print(type(6))
print(type(10/5))

#expontiation
print(2**3)

#assigning variables
x=5
y=x**2
print(y)

#string
a1 = "Hello" #equivalent to a = 'Hello'
a = "Hello how're you?"

#arithemtic operations on strings
print(a+"I'm fine, thank you.")

#multiplication of string
print(a*5)

#concatenation
b = "I'm good, thank you."
print(a+" "+b)

#division
#print(a/b)

#indexing and slicing
#first element
print(a[0])

#last element
print(a[-1])

#slicing
print(a[0:5])

#how many characters does our string have?
print(len(a))
print(f'Our string a has {len(a)} characters')

#alternatively
print('Our string a has {} characters'.format(len(a)))

#logical statement
print(2==2)

print(2==3)

print(True==1) #check if True and 1 are in fact equiavalent

print(2==2 and 3==3)
print(2==3 or 3==4)

#Testing for inequality
print(2!=3) #True

#Testing for less than/more than
print(2<3) #Trues
print(2>3) #False