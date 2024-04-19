#conditional statment's
# if and else
# if elif and else
#nested if

# if(3>4):
#     print("3 is greater than 2")
# elif(3>5):
#     print("3 is greater than 5")
# elif(3>6):
#     print("3 is greater than 6")
# else:
#     print("3 is less than 4")


#single line condition statments/ternary operator


#syntax
#variable = true_value if (condition) else false_value
#<str> if <condition> else <str>
# x= input("i love you, will you be mine : ")
# answer= "yes" if(x=="yes") else "no"
# print(answer)
# print("aman") if(x=="yes") else print("sorry")

# In Python, the ternary operator is a conditional expression also known as the "conditional expression" or "ternary conditional operator". It provides a concise way to write conditional statements.

# The syntax for the ternary operator in Python is:
# <expression_if_true> if <condition> else <expression_if_false

# print("yes you can drive") if int(input("enter your age : ")) >=18 else print("no you cannot drive")
   
#wap to input two number and print there sum 
#ans----
# a=int(input("enter first number : "))
# b=int(input("enter second number : "))
# print(a+b)


# #wap to check wether a email is correct or not 
#ans---
# print("your email is correct") if str(input("enter your email address : ")).endswith("@gmail.com") else print("your email is not correct")#endswith method to check that in string the specifc suffix os presnt or not  


#wap to check wether number entered by user is odd or even
#ans--
# number = int(input("enter the number : "))
# print("number is even") if number % 2 == 0 else print("number is odd")
#wap to find greatest of 3 numbers
#ans--
# a=int(input("enter first number : "))
# b=int(input("enter second number : "))
# c=int(input("enter third number : "))
# print("a is greater") if a>b and a>c else print("b is greater") if b>a and b>c else print("c is greater")


#wap to check wether a number is a multiple of 7 ?
# #ans---
# number=int(input("enter the number : "))
# print("it is mutiple of 7") if number%7==0 else print("it is not multiple of 7")
#string are imutable they cannot be chaged once declared




#list in python 
#is s bulit in data type capable of storing mutiple datatypes together syntax list=[]
#list are mutable they can be changed


#wap program to print student name marks and class from data
# name_of_student=["aman","suraj","ali","ketan","vishwas"]
# marks=[80,80,80,80,0]
# clas=["12th","12th","12th","12th","09th"]
# for i in range(5):
#     print(name_of_student[i],"----",marks[i],"----",clas[i])
# print(len(name_of_student))
#append----add in last  
#remove----remove the first occuring selected element 
#insert(idx,el)--- add elements at selected index 
#pop-----remove the elemet from the selected index
# list=[1,2,3,4,5,6,7,8,9]
# print(list.append(4))



#wap to take 3 movies name from the user and store it into a list
# list=[]
# for i in range(3):
#      list.append(str(input("enter your faviorate movie name :")))
# print(list)

#wap to check whether the list  is palindrom or not
# list1=[1,2,1]
# list2=["1","abc","abc","1"]
# nlist1=list1.copy()
# nlist2=list2.copy()
# nlist1.reverse()
# nlist2.reverse()
# print("palindrom") if nlist1==list1 else print("not palindrome")
# print("palindrom") if nlist2==list2 else print("not plaindrom")



# #wap to check how many student form list get a grade 
# list=["A","A","B","C","F","A","B","B","B","B","A","C"]
# print(list.count("A"))
# # 2nd part of question
# #store the above value in list and stort them from "A->D"
# list2=list.copy()
# list2.sort()
# print(list2)




#tuple
# tuple=(1,2,3,4,"hello","shanti")
# print(tuple)
# print(type(tuple))
#methods----count,index,append,remove

# tuple=(1,2,3,4,5,6,7,8,9)
# mode=list(tuple)
# mode.append(4)
# tuple(mode)
# print(mode)


#nested dictionry
# dict={"name":"aman","subjects":{
#     "python":"45",
#     "dsa":"42",
#     "physics":"39",
#     "maths":"43",
#     "aiml":"46"
# }}
# dict["name"]="monica"
# print(dict["subjects"]["maths"])
# dict.update({"name":"aman"})
# print(dict["name"])

#sets
# set={1,2,2,2,2,2,3,4,5,"hwl","paji"}
# print(set)
# set1={1,2,3,4,5}
# set2={6,7,8,9,10}
# print(set1.union(set2))
#wap to check number of student with same name in a list
# list=["aman","aman","hello","shanti","shanti","ketan"]
# my_set=set(list)
# my_set.count("")
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)


#wap to find all prime number b/w 1-100?
# for i in range(2,100):
#     prime=True
#     for x in range(2,i):
#         if i%x==0:
#             prime=False
#             break
#     if prime:
#         print(i,"is a prime")
#     else:
# #         print(i,"is not a prime")

#printing version of python 

# import sys
# print(sys.version)

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2

# Perform element-wise multiplication by 3
result_list = [i * 3 for i in concatenated_list]

print("Result after concatenation and element-wise multiplication by 3:", result_list)

