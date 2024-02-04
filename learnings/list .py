# learning about list in this slide


# how do we declare  a list ?
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list have multiformat support
mylist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, "dog", "cat", "tiger"]


# indexing in list
# it begins with zero
print(mylist[0])
print(mylist2[9])

#how to check number of elements in a list
#method1
print("number of elements in the list is ",len(mylist))
#method2
count =0
for i in mylist:
    count +=1
print("number of elements in list using method 2 is : ",count)
# some if else with list
if "dog" in mylist2:
    print("yes its present")
else:
    print("no its not ")

    # now how to check number of elements in a list
    # the morden way
print("so length of mylist2 is :", len(mylist2))
print("length of mylist is :", len(mylist))


# 4 TYPES OF METHOD IN A LIST ]]

# 1
# append(x): Adds an element x to the end of the list.
mylist.append(23)
print(mylist)
# by using append you can add any type of data in list
mylist.append("hellokitty1")
print(mylist)

# 2
# insert(i, x): Inserts an element x at the specified position i.
# mylist.insert(i,element) i is index of insertion in list
mylist.insert(0, "hellokitty2")
print(mylist)
# even if a element is already present at the insertion point .insert shift all elements next to the insertion point to next corrospoinding indexing making the postion vacant


# 3
mylist.remove(23)
print(mylist)
