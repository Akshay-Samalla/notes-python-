'''


4) You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order
'''

numbers=[1,2,3,4,5,6]
numbers=filter(lambda x:x%2==0,numbers)
numbers=list(numbers)
numbers=map(lambda x:x*2 if x%2==0 else x , numbers)
numbers=list(numbers)
print(numbers)