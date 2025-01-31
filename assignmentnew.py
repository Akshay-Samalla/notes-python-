# # find the area of the rectangle using the input , type conversion and formatted string
# test user is lower and password is password123 then login success 
# check the given number is prime or not 
# calculate the tax based on the salary if salary is less than 5 lpa then tax is 10% else 20% gross=net+allowance
# calculate attendance tracker based on number of classes attended and show attendance is not sufficient
# and not allowed to take the exam

length = int(input('enter the length: '))
width = int(input('enter the width '))
area = length * width 
print(f'area of the rectangle is : {area}')

net_salary=int(input("enter the net salary "))
allowance=int(input("enter the allowances "))
gross_salary=net_salary+allowance
print(f'net salary {net_salary}')
print(f'allowance {allowance}')
if gross_salary < 500000:
    tax= gross_salary * 0.1
    print(f"tax: {tax}")
else:
    tax= gross_salary * 0.2
    print(f"tax: {tax}")


total_classes=int(input("Enter the total number of classes : "))
attended_classes=int(input("Enter the number of attended classes : "))
percent=(attended_classes / total_classes) * 100
if percent >= 75:
    print("Allowed for the exam")
else:
    print("not allowed for the exam")

count=0
num=int(input("enter a number : "))
for i in range(1,num+1):
    if num%i==0:
        count+=1
print("prime") if count==2 else print("not a prime")



count = 3
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check if the credentials are correct
    if username == "testuser" and password == "Password123":
        print("Login successful!")
        break
    else:
        count -= 1
        if count > 0:
            print(f"invalid credentials {count} times left")
        else:
            print("The number of attempts are  completed. Try again after later ")
            break
        
        