#synatx of dictonary
#it have special feature in compare to list and tuple which is it have key-value pair means every key have a value or every value have key example name : aman age : 18 
mydict={"name":"Vinod","age":"28","course":"B.tech","specialization" :"LM"}
#rember dic is mutable you can remove and add key value pairs in it 
print(mydict)
#printing specific value by using key 
print(mydict["name"])


#adding new key-value pair
mydict["email"]= "xyz@gmail.com"

print(mydict)

#changing value of a key form dic
mydict["name"] ="sam"
print(mydict)

#removing entery form dictionary 
mydict.pop("name")
print(mydict)

#to check whether key exist or not 
if "age" in mydict :
    print("true")