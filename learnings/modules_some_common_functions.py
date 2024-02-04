# import sys
# # In Python, sys is a module that provides access to some variables used or maintained by the Python interpreter, as well as functions that interact strongly with the interpreter. It is part of the standard library

# #some common function in sys :

# #knowing the size in bytes of any data structure
# mytuple=[1,2,3,4,5,6,7,8,9,10]
# mylist=[1,2,3,4,5,6,7,8,9,10]

# print("size of my tuple is ",sys.getsizeof(mytuple),"bytes")
# print("size of my lst is ",sys.getsizeof(mylist),"bytes")
# a =int(4)
# b=4
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))


#timeit module 
#timeit method (function) : it just repeats a process n times and then calculate time taken to peprforme the task 

#for ex  tuple and list are almost same(not fully same) but lest see which data structure requires less time to create 
import timeit
print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=100000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=100000000))

#you can see the results that is much easier and faster to create a tuple then a list like tuple take 1/3 less time as of list to get generated 





