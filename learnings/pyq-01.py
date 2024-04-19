# #q-7
# total = 0
# while total <= 50:
#     x = int(input("Enter a number: "))
#     total += x
#     print("Total is:", total)


#or
# number=int(input("enter a number :"))
# prime=True
# if number <=1:
#     print("no,it is not a prime")
    
# else :
#     for i in range(2,number):
#         if number % i== 0:
#             prime=False
#             break
#     if prime:
#         print("yes,it is a prime")
#     else:
#         print("no,its not a prime")
 
# #q1
# list1=["hqll",1,"j"]
# list2=["hqllo",12,"s"]
# print(list1+list2)




#in inheritance there is parent child relation ship between two or more classes 
#the child class  will inherit all the properties and behaviors of the parent class 

#*******simple inheritance**********



class parent1:
    def m1(slef):
        print("parent1 method")
class parent2:
    def m2(slef)
    
    :
        print("parent2 method")
class child(parent1,parent2):
    def m3(slef):
        print("parent1 method")