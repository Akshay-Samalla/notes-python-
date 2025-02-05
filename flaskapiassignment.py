
#type : None
from flask import Flask , request ,  jsonify 
from flask_cors import CORS 
import mysql.connector as con 
from mysql.connector import Error
app = Flask(__name__)
CORS(app)

try :
    connection = con.connect(
       host='localhost',
       user="root",
       password="12345",
       database="lol" 
    )
    cursor = connection.cursor()
    
    if connection.is_connected():
        print('database connected')
        
    
except Error as e:
    print('error ',e)
    
@app.route('/students',methods=['GET'])
def get_students():
    cursor.execute('SELECT * from students')
    students=cursor.fetchall()
    return jsonify(students)
      


'''

create table students (
id int auto_increment primary key,
name varchar(100) not null,
email varchar(100) unique not null,
age int not null,
rollNumber varchar(100) unique not null,
department varchar(100) not null,
phoneNumber varchar(17) not null,
gender varchar(6) not null
);

'''
@app.route('/students' , methods=['POST'])
def post_students():
    data=request.json
    name=data['name']
    email=data['email']
    age=data['age']
    rollNumber=data['rollNumber']
    department=data['department']
    phoneNumber=data['phoneNumber']
    gender=data['gender']    

    cursor.execute(
        '''insert into students 
        (name,email,age,rollNumber, department , phoneNumber, gender)
        values (%s,%s,%s,%s,%s,%s,%s)
        
        ''',
        (name , email ,age, rollNumber, department, phoneNumber , gender)
    )
    connection.commit()
    return jsonify({'message':'user added successfully'})

    
@app.route('/students/<int:id>',methods=['GET'])
def get_student_by_id(id):
    cursor.execute('SELECT * from students where id =%s',(id,))
    students=cursor.fetchone()
    if students:
        return jsonify(students)
    return jsonify({"message":"user not found"}),404
      
@app.route('/students/<int:id>' , methods=['PUT'])
def students_update(id):
    data=request.json
    name=data['name']
    email=data['email']
    age=data['age']
    rollNumber=data['rollNumber']
    department=data['department']
    phoneNumber=data['phoneNumber']
    gender=data['gender']    

    cursor.execute(
        '''update students set
        name=%s,email=%s,age=%s,rollNumber=%s, department=%s , phoneNumber=%s, gender=%s where id=%s
        
        ''',
        (name , email ,age, rollNumber, department, phoneNumber , gender    ,id)
    )
    connection.commit()
    return jsonify({'message':'user updated successfully'})

@app.route('/students/<int:id>',methods=['DELETE'])
def delete_student_by_id(id):
    cursor.execute('delete  from students where id =%s',(id,))
    connection.commit()
    return jsonify({"message":"user deleted successfully"}),404
      

if __name__ == '__main__':
    app.run(debug=True)                                                                           