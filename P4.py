import func
user= "Teacher"
password= 1234
#User Authentication
for i in range(3):
    uname= input("Enter your Name:")
    upassword= int(input("Enter your password:"))
    if (uname==user and upassword==password):
        print("Welcome")
        students = {1: "A",2: "B",3: "C",4: "D"}
        print("1. Details of Students")
        print("2. Add Student")
        print("3. Update Student Details")
        print("4. Delete Student")
        n=int(input("Enter your choice:"))
        if (n==1):
            print(students)
        elif(n==2):
            a=int(input("Student Registration Number:"))
            b=input("Name of Student:")
            students[a]=b
        elif (n==3):
            a=int(input("Student Registration Number:"))
            b=input("Name of Student:")
            students.update({a:b})
        elif (n==4):
            a=int(input("Student Registration Number:"))
            students.pop(a)
        else:
            print("Invalid Choice")
        break
    else:
        print("Wrong Credentials")
# Marking attendence
print("1. Attendence to Student A ")
print("2. Attendence to Student B ")
print("3. Attendence to Student C ")
print("4. Attendence to Student D ")
n= int(input("Enter your choice:"))
if (n==1):
    e=func.A()
    print("Attendence of Student A:",e)
elif(n==2):
    f=func.B()
    print("Attendence of Student B:",f)
elif (n==3):
    g=func.C()
    print("Attendence of Student C:",g)
elif (n==4):
    h=func.D()
    print("Attendence of Student D:",h)
else:
    print("Invalid Choice")
    


    
    
