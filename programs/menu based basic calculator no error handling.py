# question wapr to create a basic menu driven basic calculator 
#input logic for number
num1= int(input("your first number :"))
num2 =int(input("your first number :"))
#menu based ask?
print("******************************menu*******************************")
print("***please select one option from below to perform action***")
print("***option : 1 add***")
print("***option : 2 minus***")
print("***option : 3 multiply***")
print("***option : 4 divide***")
inv=int(input("select the operation you wana do with your numbers :"))

#logic for opertional menu
#number based
#select the option
#1.add 2.minus 3.multiply 4.divide
def check(inv):
    if(inv==1):
        print(num1+num2)
    elif(inv==2):
        print(num1-num2)
    elif(inv==3):
        print(num1*num2)
    elif(inv==4):
        print(num1/num2)
    else:
        print("SELECT THE OPTION CORRECTLY THERE IS MISTAKE IN SELECTION")
check(inv)