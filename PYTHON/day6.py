'''



















class Employee :
    company_name = 'abc corp'
    def __init__(self, name , age):

        self.name=name
        self.age=age
    @classmethod 
    def change_company_name(cls,new_name):
        cls.company_name = new_name 
    def display_info(self):
        print(f'name:{self.name}, age:{self.age},comany:{Employee.company_name}')
#creating instances
emp1= Employee('alice',30)
emp2=Employee('bob',77)

emp1.display_info()
emp2.display_info()

emp1.change_company_name('psych')
emp1.display_info()
emp2.display_info()


class Example:
    def __init__(self,*args ):
        if len(args)==1:
            print(f'hello {args[0]}')
        elif len(args)==2:
            print(f'hello {args[0]}, you are {args[1]} years')
example1= Example('psych')
example2= Example('psych', 88)



class Example2:
    def __init__(self,**kwargs):
        if 'name' in kwargs and 'age' in kwargs:
            self.name=kwargs['name']
            self.age=kwargs['age']
            print(f'kwargs {kwargs['name']} , {kwargs['age']}')
        elif 'name' in kwargs:
            print(kwargs['name'])
    def display(self):
        print(f'hello {self.name}, {self.age}')
example1= Example2(name='psych')
example2= Example2(name='pysch',age=100)
example2.display()




class Employee:
    def __init__(self, name , designation):
        self.name=name
        self.designation= designation
    def get_employee_details(self):
        print(f'employee name: {self.name} designation  {self.designation}')
class ContractEmployee(Employee):
    def __init__(self , name , designation , contract_period):
        super().__init__(name, designation)
        self.contract_period= contract_period
    def get_contract_employee_details(self):
        super().get_employee_details()
        print(f'contract period is {self.contract_period}')

contract_employee= ContractEmployee('geetha','senior trainee',234)
contract_employee.get_employee_details()
contract_employee.get_contract_employee_details()










































class Father:
    def __init__(self):
        print('father class constructor')
    def showf(self):
        print('father class method')
class Son(Father):
    def __init__(self):
        super().__init__()
        print('son class constructor')
    def shows(self):
        print('son class method')
class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print('GrandSon class constructor')
    def showg(self):
        super()
        print('grandson class method')
grandson=GrandSon()
grandson.showf()
grandson.shows()
grandson.showg()




class Father:
    def __init__(self):
        print('father class constructor')
    def showf(self):
        print('father class method')
class Son(Father):
    def __init__(self):
        print('son class constructor')
    def shows(self):
        print('son class method')
class Daughter(Father):
    def __init__(self):
        print('daughter class constructor')
    def showd(self):
        print('daughter class daughter')
d=Daughter()
d.showd()       
d.showf()
s=Son()
s.shows()
s.showf()






'''







class Father:
    def __init__(self):
        super().__init__()
        print('father class constructor')
    def showf(self):
        print('father class method')
class Mother:
    def __init__(self):
        super().__init__()
        print('mother class constructor')
    def showm(self):
        print('mother class mehtod')
class Son(Mother , Father):
    def __init__(self):
        super().__init__()
        
        print('son class constructor')
    def shows(self):
        print('son class method')
s=Son()
s.showf()
s.showm()
s.shows()
print(Son.mro())   #method resolution order it will show the order of the classes 


'''multilevel inheritance with car or vehicle '''

class Vehicle:
    def __init__(self,no_of_tyres,body_type,Category):
        self.no_of_tyres=no_of_tyres
        self.body_type=body_type 
        self.category=Category
    def get_vehicle_details(self):
        print(f'tyres : {self.no_of_tyres}, body type: {self.body_type} , category: {self.category}')
class Car(Vehicle):
    def __init__(self,no_of_tyres,body_type,Category,car_name , Start , Stop , Horn, Lights):
        super().__init__(no_of_tyres,body_type,Category)
        self.car_name=car_name 
        self.start=Start
        self.stop= Stop
        self.horn = Horn 
        self.Light = Lights
    def start_car(self):
        print('car started',self.start)
    def stop_car(self):
        print('car stop',self.stop)
    def lights(self):
        print('car lights',self.Light)
    def horn_car(self):
        print('horn car',self.horn)
class Toyota(Car):
    def __init__(self,no_of_tyres,body_type,Category,car_name , Start , Stop , Horn, Lights,car_model):
        super().__init__(no_of_tyres,body_type,Category,car_name , Start , Stop , Horn, Lights)
        self.car_model=car_model

ragerover=Toyota(10,'steel','petroli' , "psych rage" , "starting car", "stoping car ", "peeeeep", "no",'no324')
ragerover.start_car()
ragerover.lights()
ragerover.horn_car()
ragerover.stop_car()
    

        
        
        
        
        
        
        
        
        
        
'''



create a class withe the name of vairiable it should have two functionality it should display vehicle information 
second functionality is start engine 
details like model brand year 
inherit vehicle class in the car 
add two more in car display car info and open dickey or trunk 
category : disel , petrol ,electric (fuel type)
display electric vehicle information like charge capcity what is the KW charge battery you have 



'''

    
