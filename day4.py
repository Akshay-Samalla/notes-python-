'''

lambda function is anonymous function for single use functions


'''
#calculate the toatal amount based price and quantity as input from user 
#using lambda function

# def price():
#     quantity=int(input('enter the quantity'))
#     price=int(input('enter the price'))
#     price_calculate= lambda quantity , price: quantity*price  
#     print(f'quantity : 10 , price:10000 , total price :{price_calculate(quantity,price)}') 
# price()
# def labdaexample1():
#     add_10= lambda x:x+10 
#     print(add_10(20))
# labdaexample1()
# def lambdaexample2():
#     num1=int(input('enter the first number'))
#     num2=int(input('enter the second number'))
#     product = lambda num1,num2: num1*num2 
#     print(f'product of {num1}*{num2}={product(num1,num2)}')
# lambdaexample2()
# def lambdaexample3():
#     check_even = lambda x : 'even ' if x%2==0 else 'odd '
#     print(check_even(4))
#     print(check_even(7))
# lambdaexample3()

# def lamdawithmap():
#     numbers=[2,4,5,7,9]
#     result= map(lambda x: x*3 , numbers)
#     print(list(result))
# lamdawithmap()    

# def lamda_with_filter():
#     numbers=[1,2,3,4,5]
#     result= filter(lambda x:x>3 , numbers)
#     print(list(result))
# lamda_with_filter()

# def lambda_with_sort():
#     numbers = [11, 321 , 32, 4, 50 ]
#     print('ascending order ')
#     numbers.sort()
#     print(numbers)
#     print('descending order')
#     numbers.reverse()
#     print(numbers)
# lambda_with_sort()


# def lambdawithsorted():
#     people=[('alice',30),('bob',25),('char',35)]
#     sorted_people = sorted(people , key = lambda person : person[1])
#     print(sorted_people)
# lambdawithsorted()

# names=['Geetha', 'Jey', 'Fransy']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[-1])
# print(names[-2])

# print(names[1:])
# print(names[1:3])
# print(names[:])
# print(names[2:])
# print(names)

# #finding max element of the list
# def find_max_list():
#     numbers=[1,2,3,33,4,4,44,55]
#     max=0 
#     for i in numbers:
#         if i>max:
#             max=i
#     print(max)
# find_max_list()

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
# for row in matrix:
#     for i in row:
#         print(i) 
#     print()

# numbers=[1,2,3,4,5,6]
# numbers=append(450)
# numbers.insert(1,900)
# print(numbers)
# numbers.remove(900)
# print(numbers)
# numbers.clear()
# print(numbers)
#remove the lastitem in the list
# numbers.pop()
# print(numbers)
# to check the existance of the give value
# print(numbers.index(56))
# print(numbers.index(560))
# print(560 in numbers) # it will retrun boolean value. it wont give any error 
# numbers.append(3)
# print(numbers.count(3))
# print(numbers.count(3)) #it wil numbers items(3) found in the list
# numbers= [3,56, 67,34,66,3]
# #sort in ascending 
# print(numbers.sort()) # none
# numbers.sort()
# employees=[
#     {'name':'alice',"salary":50000},
#     {"name":"bob", "salary":60000 } ,
#     {"name": "charlie", "salary":40000,}
# ]
# sorted_employees= sorted(employees , key = lambda x: (x['salary'], x['name']))
# print(sorted_employees)
# sorted_employees= sorted(employees , key = lambda x: (-x['salary'], x['name']))
# print(sorted_employees)


# from functools import reduce
# numbers=[1,2,3,4]

# product=reduce(lambda x,y : x*y , numbers)
# print(product)



#unpacking 
numbers=(1,2,3)
x,y,z=numbers 
x,*others=numbers 
print(x,others)
print(type(others))



def display(a,b):
    yield a 
    yield b  
x=display(10,20)
print(list(x)) 

def fetch_orders_in_batches(orders, batch_size):
    for i in range(0, len(orders), batch_size):
        yield orders[i:i+ batch_size]
orders=[101,102,103,104,105,106,107,108,109]
for batch in fetch_orders_in_batches(orders,3):
    print('processing batch', batch)

customer= {
    "name":"geetha eshwarmurthi",
    "email":"geetha@gmail.com",
    "phone":45677,
    "age":23,
    "is_verified":True 
}
print(customer['name'])
print(customer.get('name'))
print(customer.get('birthdate'))
print(customer.get('birthday','1/2/2'))
print(customer)
customer['name']='Riya Sam'
print(customer)
customer['location']='chennai'
print(customer)












