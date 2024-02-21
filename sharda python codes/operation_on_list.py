L1=[12,23,23,56,67,24]
# find number of elements in the list
#method 1
print(len(L1))
#method 2

#b. remove 3rd element
L1.remove(23)
print(L1)
#add 33 at index position 0
L1.insert(0,"33")
print(L1)
# add 99 at the end of the list
L1.append(99)
print(L1)
#search for `67' in the list and if it exists print its index position
for i in range(0,6) :
    if L1[i]==67 :
        print("element found at index postion :",i)