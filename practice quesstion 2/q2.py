'''

2)student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
    List the name which has more than 6 characters as lone_names list using appropriate function


'''


student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
lone_names=filter(lambda x:len(x)>6,student_name_list )
print(list(lone_names))