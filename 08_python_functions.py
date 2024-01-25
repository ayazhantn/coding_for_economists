#let's talk about functions

#function definition syntax
def add_one(num):
  return num+1

print(add_one(1))

#function without return statement and without arguments
def add_one_str():
  print(6)

print(add_one_str())

#try to assign the output of a function to a variable
res=add_one(5)
res_str=add_one_str()
print(res, res_str) #(6 None)

#multiple return values
def add_one_return_both(num1):
  return num1, num1+1

print(add_one_return_both(5)) #(5, 6)

print(type(add_one_return_both(5))) #<class 'tuple'>

#more than one argument in functions
def add_two_nums(num1, num2):
  res=num1+num2
  return num1, num2, res

print(add_two_nums(5, 6))

#default values for function arguments
def exponentiate(num, exponent=2):
  return num**exponent

print(exponentiate(2))
print(exponentiate(5,2) == exponentiate(5)) #true
print(exponentiate(5,3) == exponentiate(5)) #false

#keywords arguments: using the argument name to assign a value; here, order does not matter
print(exponentiate(exponent=1, num=2)) #2


#functions with variable number of arguments
def add_nums(*nums):
  res = 0
  for num in nums:
    res+=num
  return res

print(add_nums(1,2,3,4,5,6,7,8,9,10)) #55



#lets' try to coe up some docstrings for a function
def cast_listitems_to_str(list_of_objects):
  """
  Casts all items in a list to list of string.

  Parameters:
  -----------------
  list_of_objects: list

  Returns:
  -----------------
  list_of_strings: list
  """
  list_of_strings=[]
  
  for element in list_of_objects:
    list_of_strings.append(str(element))
  return list_of_strings

lst=[1, 2, '4']
print(cast_listitems_to_str(lst)) #['1', '2', '4']

#print(help(cast_listitems_to_str))

#print(list_of_strings) #NameError: name 'list_of_strings' is not defined - it is inside the function

#scope of a variable
def test(a,b):
  c=a+b #scope of 'c' is confined to function
        # 'c' is said to have local scope
  return(c)

c=5 #here, 'c' has global scope

# lambda functions (aka anonymous functions)
# reference function
def square(x):
  """
  Returns the square of x

  Parameters:
  -----------------
  x: int or float or double

  Returns:
  -----------------
  square_x: int or float or double
  """
  return x**2

# equivalent lambda function
square_lambda = lambda x: x**2

#compare output
print(square(5) == square_lambda(5))