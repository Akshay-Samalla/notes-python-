'''

break : is used to jump out of the loop or iteration 
continue is used to go back to the begining of the loop
pass lets to ignore the block which can be written later 

'''
n=5
i=1
while i<5:
    if i>3:
        break 
    print(f'i value is {i}')
    i+=1
print(f'i value after loop over {i}')

counter=1
max=10
if counter <= max :
    counter += 1 
else:
    pass 
print('end of the program')


'''

ternery operator : trueblock if condition else elseblock 


'''
# without ternary operator 
age=int(input('enter you age:'))
ticket_price=0
if age>=18:
    ticket_price=20 
else:
    ticket_price=5
print(f'the ticket price is {ticket_price}')

#with ternary operator 
age=int(input('enter the age'))
ticket_price= 20 if age>=18 else 5
print(f'ticket price is {ticket_price}')



'''

python functions  
a function is a named code block that performs a job or returns a value 

'''
#function without parameter
def greetCustomer():
    ''' just function demo'''
    print('hey , welcome to function in python')
greetCustomer()

#function with  parameter
def greetUser(name):
    print(f'hey {name}, welcome to international conference')
greetUser('Geeta')

#function with more parameter with return statement 
def add(num1 , num2):
    sum= num1 + num2 
    return sum 
addition_result = add(100,900)
print(f'addition result = {addition_result}')

#function with default parameters
def getEmployeeInfo(name='Geeta', designation='Senior consultant'):
    print(f'name:{name}\ndesignation={designation}')
getEmployeeInfo()
getEmployeeInfo('hara','trainer')
getEmployeeInfo('geetha')
getEmployeeInfo(designation='trainer',name='getha')


def customerInfo(name ,salary , location = 'hyderabad'):
    print(f'customer name:{name} \n location ={location}')
customerInfo('mali',90000)

'''

python lambda expression allow you to write anonymous functions 

'''