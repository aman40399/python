#functions block of statment which performs a specific task when called 
#why do we need function at first place ans- to reduce reduncey and increase reusablity 
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
def printo(n):
    print(n)
    if n==0:
       return
    else:
     printo(n-1)
printo(8)

#you can also set default values for a function 
#example 
def aman(a=0,b=8):
    print(a+b)
#in this case if you just call the function without passing any value default values will be selected a=0 and b=8

#write a program which take as may as number and print the average of the numbers 

#In this function, *numbers allows you to pass any number of arguments when calling my_function. These arguments will be packed into a tuple named numbers.
# def average(*number):
#     sum=0
#     for i in number:
#         sum+=i
#     print("average of the number are ",sum/len(number)) 
# average(2,4,5,6,7,8,9,0,0)   

#lambda functions : are anynoumous functions which takes certain argument and preforms the expression  
# syntax lambda arguments : expressions 
#example 
# ans=lambda x,y,z :x+y+z
# print(ans(1,2,3))
#output is 6 in int datatype
#u can also [pass] function inside functions example 
# cube = lambda x :x*x*x
# square =lambda x:x*x
# def appl(x,fx):
#     return print(fx(x))

# appl(5,cube)


