#oops-object orineted programing
# OOPs Concepts in Python
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# Data Abstraction
#-----------------------------------------------

#class 
#so  class is a blueprint of creating objects

# class Nameclass:
#     pass
#attributes in class are nothing but variables in of class which can be accessed by using dot.method(in side object) , eg-Nameclass.attribute_name

#what do we get when we try to print a class
# class Nameclass:
#     pass
# print(Nameclass)

#<class '__main__.Nameclass'>

#where __main__ is the name of the  module
#Nameclass is the name of the class
#notes 
''' 
so function/def inside of class is known as methods
and variable inside of a class is knwon as attributes  '''

#-----------------------------------------------------------------------------------

#object
#object is nothing but instance of a class
#object is created by calling the class
# class Nameclass:
#     pass
# obj=Nameclass()

#what we get when we try to print object
# print(obj)
#<__main__.Nameclass object at 0x000001E63558E15000>
#where main is the name of the module
#Nameclass is the name of the class
#object is the name of the object
#0x000001E63558E15000 is the memory address of the object



# class froum:
#     name='x'
#     age=0
#     gender='male'
#     def info(self):

#       print(self.name,"is a",self.gender,"of age",self.age)
   #objects   
# a = froum()
# b = froum()
#change in objects
# a.name='aman'
# a.age=19
# a.gender='male'
#calling function
# a.info()
# b.info()

# Constructor:
# __init__ -> It's a special method in Python classes that serves as a constructor.
#            When an instance of a class is created, the __init__ method is automatically called.
#            Its purpose is to initialize the object's attributes and any other setup that needs to be done.
#            You can think of it as the method that gets executed when the object is "constructed" or "instantiated".

# class MyClass:
#     def __init__(self,agr3,arg1, arg2):
#         # Initialize attributes or perform any necessary setup here
#         self.name=agr3
#         self.marks1 = arg1
#         self.marks2 = arg2

# Creating an instance of MyClass, which automatically triggers the __init__ method
# my_instanceobj = MyClass(10, 20)
#now constructor are of two types
#1. default - this take only self as input parameter
# 2. parametrized - this takes arguments and self both 

#polymorphism
#in simple terms, polymorphism is about having different classes respond to the same method or request in their own unique way.
#example
# class sem1:
#     def __init__(self,a,b):
#      self.name= a
#      self.person= b
#     def info(self):      
#        print(f'{self.name} is a {self.person}')
# class sem2:
#     def __init__(self,bname,b):
#      self.name=bname
#      self.person=b
   
#     def info(self):
#        print(f'{self.name} is not  a {self.person}')
# obj1=sem1('aman','male')
# obj2=sem2('monica', 'male')

# obj1.info()
# obj2.info()



#in this case above we have two class and a method of same name which perform diffrent functions which aligns woth idea of plymorfism which mean diffrent class responds to same method in there unique way

#encapsultaion
#so encapsulation is a fundamental concept in oops , which contains data(attributes) and function(methos) into a single unit called as class, then only exposing public interface to interact with object and code remains hidden 

#why we encapsulate the code?
#1.data protection , reuse and redablity acess control safe change 


#how to achieve it ?
#it can be achived using private attributes ? what is a private attribute .
#so there are the varibles in side of class which cannot be directly acccessed like we do after creating an object (instance) for example 


#regular method to access the attributes outside of the class which is the object side 
class Froum:
    def __init__(self,oname,oage):
      self.name = oname
      self.age = oage
 
obj1=Froum('aman','CSI')
print(obj1.name)

#but now if we use private attributes instead of regular one u will see its not possible to access it directly aka encapsulation of the data    

class Froum:
    def __init__(self,oname,oage):
      self.__name = oname #this is private attribute now
      self.age = oage
 
obj1=Froum('aman','CSI')
print(obj1.__name)

