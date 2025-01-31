print('hi')
import keyword
print(keyword.kwlist)
str='hi its me "harry potter"'
stri = "hi it's harry potter "
strin= '''
hey its me harry potter
hey its me ron weesely
hey its me harmoine granger
'''
pathstri= r"C:\Users\aksha\Desktop\New folder (2)"
print(str , stri , strin , pathstri)

#CONCATINATION
concatinatioin = 'hi' 'how are you'
print(concatinatioin)
conatiniation =  'we'+'re'
print(conatiniation)
fname = "harry"
lname = "potter"
fullname = "namskar "+ fname + lname + ' welcome'
print(fullname)
print(fullname[5:])

#declaring and initializing variable
#individual
a=10
b=10.23
c='python example'
d="python example"
#multiple
e,f,g,h= 10, 10.23, "python example",'python example'
#multiple with same value
i=j=k=l=m=n= True

print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',h,'\n',i,'\n',j,'\n',k,'\n',l,'\n',m,'\n',n)
print('$'*30)
a,b=4,2
#addition
print(f'a+b={a+b}')
#subtraction
print(f'a-b={a-b}')
#multiplication
print(f'a*b={a*b}')
#exponent
print(f'a**b={a**b}')
#division
print(f'a/b={a/b}')
#modulo division
print(f'a%b={a%b}')
#floor division
print(f'a//b={a//b}')

print(f'5>2 = {5>2}')
print(f'5>=2={5>=2}')
print(2<3 or 2  or 3)

str1 = "hi harry potter how are you"
str2 = "we are here ron"
str3 = "hi harmoini"
print('hi' in str1)
print('hi' in str2)
print('hi' in str3)

'''
operator precedence
()
**
+,-,~
*,/,//,%
+,-
<<,>>
&
^
>,>=,<,<=,==,!=
=,%=,/=,=//,-=,+=,*=,**=
is ,is not
in , not in
not
or
and

'''
#type conversion implicit
a=5
b=2
value = a/b
print(value)
print(type(value))
#type conversions explicit
a=10
float_value= float(a)
print(float_value , type(float_value))
str='10'
print(str , type(str))
a=a+int(10)
print(a,type(a))
a_tuple=tuple(str)
print(a_tuple , type(a_tuple))
a_list = list(a_tuple)
print(a_list , type(a_list))
a=1+9j
print(a,type(a))
# a=10
# print(a,complex(a))

a=[1,2,3,4]
print(a,234,sep='* ',end='ends  ')
name='harry potter'
print("hello {} how are you".format(name))

name=input("what is you name: ")
print(name)
reg=int(input("enter your reg number"))
print(reg,type(reg))

#take the employee names using input
employee_name=input('enter the employee name (space-separated)').split()
print('************ Employee Names List **********************')
print(employee_name)
for emp in employee_name:
    print(emp)

length = int(input('enter the length :'))
width = int(input('enter the width :'))
print(f'area of rectangle is {length * width}')

# find the area of rectangle using the type conversion and formated string

language='python'
if language.lower() =='python':
    print(language.upper())
print(language.capitalize())


import dis
def add(a,b):
    sum=a+b
    return sum
result = add(10,20)
print(f'result of add(10,20):{result}')
print('disassembly')
dis.dis(add)




while True:
    language=input('what is the programming language')
    if language.capitalize()=='Python':
        print(f'you are right its {language}')
        print('still here')
        break
    else:
        print('not good')
#take username and password form the user and 


#prime number 
n=int(input())
