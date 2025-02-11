# keys=['name','age','city']
# values=['alice',35,'new york']
# my_dict = dict(zip(keys,values))
# print(my_dict)

# '''

# TUPLE:
# immutable 
# ordered 
# () 
# heterogeneours 
# tuple * 3 (same tuple elements three times)
# to create a tuple with single value it should be followed by a comma ',' => tuple=(9,)


# '''
# data=(1,2,3)
# print(data)
# print(data[1])
# b=(1,2,3)
# result=b*3
# print(result)

# tuple1=(4,)
# print(tuple1)



# '''

# SET :
# unique elemenets 
# mutable 
# unordered 
# no access by index 
# empty set by set()
# can contain any type except mutable elements like list or set 


# '''
# #creating an empty set
# x=set()
# #creating set with elements 
# a={10, 20 , 'python code ' , 'raj' , 40 }
# #cant access using index 
# #print(a[0]) #this shows error
# print(a)
# print(id(a))
# print()
# #duplicates are avoided 
# b={10,20,'python code'  , 'raj', 40 , 10 , 10}
# print(b)
# print()

# #adding one element 
# # a={1,2,'python' ,'code',4,1,2,2,4,3}
# a.add('python')
# print(a)
# print(id(a))
# print()

# #adding multiple elements 
# print('adding multiple elements')
# a.update([101,102,103])
# print(a)
# print(id(a))
# print()

# #deleting element using discard() method 
# a.discard('python code')
# print(a)
# print(id(a))
# print()


# #deleting element using remove() method 
# # a.remove(32)
# a.discard(324)
# print(a)
# print(id(a))


# a=set()
# print(id(a))
# n=int(input('enter number of elements: '))
# for i in range(n):
#     el=input('enter  element')
#     a.add(el)


# # a={10,20,'python code'}
# for i in a :
#     print(i)
    
# a={'allu sita rama raju' , 'bob junior' , 'kathi kanta rao'}
# b={'bob junior' , 'mahesh bob' , 'mufasa bob', 'balya', 'kathi kanta rao'}

# print('a',a)
# print('b',b)
# print()

# #intersection 
# ism=a.intersection(b)
# print('intersection ', ism )
# um = a.union(b)
# print('uninon' , um)

# dm=a.difference(b)
# print('difference :', dm)
# print()

# isub =a.issubset(b)
# print(isub)

# isup = a.issuperset(b)
# print(isup)

# b=a.copy()
# print(id(b))
# print(id(a))

# a.clear()
# print(a)




'''

the class name can be any identifier 
it can't be python reserved word 
a valid calss name starts with a letter , followed by any number of letter or underscore 

class Mobile:
    def __init__(self):
        self.model='Real Me X'
    def show_model(self):
        print('Model', self.model)
realme = Mobile()
realme.show_model()

class Myclass:
    def show(self):
        print('print method from my class')
myclass = Myclass()
myclass.show()


class Emplooyee:
    def __init__(self , name , gender , salary):
        self.employeeName=name
        self.gender=gender
        self.salary=salary 
    def get_employee_info(self):
        print(f'name: {self.employeeName} \nGender = {self.gender} \nsalary= {self.salary}')
employee1=Emplooyee('yash', 'male', 50000)
employee2=Emplooyee('tina', 'female', 59000)
employee3=Emplooyee('hara', 'male', 52000)



employee1.get_employee_info()
employee2.get_employee_info()
employee3.get_employee_info()

n=int(input('enter the number of employees'))
employees=[]
for i in range(n):
    print(f'enter the details for employee {i+1}')
    name=input('enter the employee name')
    gender =input('enter the employee gender')
    salary=float(input('enter the employee salary:'))
    employee=Emplooyee(name,gender,salary)
    employees.append(employee)
for i in employees:
    i.get_employee_info()

# filter based on gender 
while True: 
    print('OPTIONS \n 1.MALE \n FEMALE')
    n=int(input())
    if(n==2):
        for i in employees:
            if(i.gender == 'female'):
                i.get_employee_info()
    elif(n==1):
        for i in employees:
            if(i.gender == 'male'):
                i.get_employee_info()
    else:
        break
female=(filter(lambda x: x.gender=='female',employees))
male=(filter(lambda x:x.gender=='male',employees))
print(list(female), list(male))
















class Car:
    total_cars=0
    def __init__(self, make , model , year, price):
        self.make=make 
        self.model=model 
        self.year=year 
        self.price=price  
        Car.total_cars += 1 
    
    
    def car_info(self):
        print(f'car info : {self.make} {self.model} {self.year} {self.price}')
        
    @classmethod
    def get_total_cars(cls):
        print(f'total cars created : {cls.total_cars}')
    
    @staticmethod
    def depricated_value(price,year):
        depricated_rate=0.20 
        value = price * ((1-depricated_rate))*year
        return value 
car1=Car(
    'toyota', 
    'camry',
    2020,
    200000
)
car2=Car(
    'honda',
    'civiv',
    2020,
    939939
)
car1.car_info()
car2.car_info()

Car.get_total_cars()

depricated_value =Car.depricated_value(25000,3)
print(f'depricated value after 3 years : ${depricated_value:.2f}')
    
    







class Army:
    def __init__(self):
        self.name='Rahul'
        self.gn=self.Gun() 
    def show(self):
        print('name:', self.name)
    class Gun:
        def __init__(self):
            self.name='ak47'
            self.capacity='75 rounds'
            self.lenght='34.3 in'
        def disp(self):
            print('gun name' , self.name)
            print('capcity', self.capacity)
            print('length ', self.lenght\
                
                )
a=Army()
print(a.name)
print()

print(a.gn)
g=a.gn
g.disp()








'''

