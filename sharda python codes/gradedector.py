print("                     *****grade system*******               ")
# taking user input
marks=int(input("enter your marks : "))
#error managment(false input)
if marks > 100 :
    print("enter the correct marks please")
elif marks < 0 :
    print("enter the correct marks please")
else : 
   
#logic for grade 
 if marks >=90 :
    print("GRADE : A")
 elif marks >=80 :
     print("GRADE : B")
 elif marks >=70 :
    print("GRADE : C")
 elif marks >=60 :
    print("GRADE : D")
 else :
    print("GRADE : F")
   