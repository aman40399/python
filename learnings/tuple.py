#list and tupels are same just basic diffrence is list are mutables while tupple are not they both support multiformat indexing

#syntax for tuple

mytuple = tuple(["hlo","kite",1,1,1,1,2,3,4,5,6,9090])
print(mytuple)

#some operations on tuple
#counting tuple
count  =0 
for i in mytuple:
    count +=1
print(mytuple)

#method2 
print(len(mytuple))

if "kite" and "hlo" in mytuple :
    print("true")
# #Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
    #remeber not is always used above both and or it just uno reverse card for the cases

#decting duplicates in a tuple 
    #method1 using function .count
    print(mytuple.count(1))

    #method2 using logic
   # Assuming 'mytuple' is the tuple you want to check for duplicates
mytuple = (1, 2, 3, 1, 4, 5, 2, 6, 7, 8, 8)

# Method 1: Using function .count
print(mytuple.count(1))

# Method 2: Using logic
count = 0
for i in range(len(mytuple)):
    for j in range(len(mytuple)):
        if i != j and mytuple[i] == mytuple[j]:
            count += 1     
print("No. of repeats in tuple:", count)

#slicing : you can silice parts of a tuple
print(mytuple)
#note :-remember tuple is imutable so u cant change the origanl tuple but you save its operation changes to some new tuple
#selection in tuple
# what is ":" in tuple so - [a:b] a is starter where index begins and b is the end index which excluded 
print("here is the tuple  with with using [1:4]:",mytuple[1:4])
#but what if we dont specify the index answer is it goes to the end [1:]
print("here is mytuple with no end index [1:]",mytuple[1:])
#we use [a::b] a is starting inde here but b is now the gap b/w selection of elements until the end 
#simply it will keep selcting elements from start to end with gap of 3 element b/w each selected elements
print("here is the tuple  with with using [1::4]:",mytuple[1::4])
#Aadding two tuples 
#they can only be added and stored new tuple no changes in orignal tuple is posssible 
mytuple2=(99,88,55,44,33,222,111)
supertuple = mytuple+mytuple2
print(supertuple)

#.index to check the index of selected element and if elemenet is reapeted it would tell the index of first occuring of selected elemenht 

print("index of element 8 is ",mytuple.index(8))

#converting tuple into list and list in tuple
mylist3=list(mytuple)
print(mylist3)
#to check its a list 
#method1 by checking type directly 
print(type(mylist3))
#method2 by changing it beacuse only list are changable and if do not give error then it tuple 
mylist3.remove(8)
print(mylist3)


