'''

9) write a program to remove the duplicates in the list
# numbers3=[2,2,4,6,3,4,6,1]



'''

numbers3=[2,2,4,6,3,4,6,1]
numbers=[]
for i in numbers3:
    if i not in numbers:
        numbers.append(i)
print(numbers)
