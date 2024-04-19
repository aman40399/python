#functions block of statment which performs a specific task 
""" 
syntax of function 
  
  def name_func(parameter1,parameter02):
         code to be exectued
      return data

"""
#some basic examples of functions
#simple function for addition 
def sum01(a,b):
    sum=a+b
    return sum

print(sum01(1,2))


# a function which do not return any data type they have by default none as return value
def hello():
    print("hello how are you")

hello()


#you can also print the type of (function) using type function 
print(type(hello))
#output is <class 'function'>


'''
functions are classified into two types :

1)built-in functions
2)user-defined function

'''
'''
examples of bulit in functions
print()
input()
type()
range()

'''

#parameter- example of print
# Using different parameters of the print function
print("Hello", "World", sep=", ", end="!\n")
'''
sep: This parameter specifies the separator between the objects. It defaults to a space character. For example, print('a', 'b', 'c', sep=',') will output a,b,c.

end: This parameter specifies what to print at the end. By default, it is a newline character (\n). You can change this behavior, for instance, to print without a newline by setting end=''.'''

#recursive function are the functions , which call's itself
#wap which print prime number only upto 'n' with help of recursive function