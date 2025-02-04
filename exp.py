import mysql.connector 
from mysql.connector import Error 
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='lol'
        )
        if connection.is_connected():
            print('connected to mysql')
        return connection
    except Error as e :
        print('error',e)
        return None
       
def create_user(name, email):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(query, (name, email))
            connection.commit()
            print("User added successfully")
    except Error as e:
        print(f"Failed to insert record: {e}")
    finally:
        if connection:
            connection.close()


# READ Operation
def get_users():
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            records = cursor.fetchall()
            for row in records:
                print(row)
    except Error as e:
        print(f"Failed to retrieve records: {e}")
    finally:
        if connection:
            connection.close()

# UPDATE Operation
def update_user(user_id, name, email):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
            cursor.execute(query, (name, email, user_id))
            connection.commit()
            print("User updated successfully")
    except Error as e:
        print(f"Failed to update record: {e}")
    finally:
        if connection:
            connection.close()

# DELETE Operation
def delete_user(user_id):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE id=%s"
            cursor.execute(query, (user_id,))
            connection.commit()
            print("User deleted successfully")
    except Error as e:
        print(f"Failed to delete record: {e}")
    finally:
        if connection:
            connection.close()

# Example Usage
if __name__ == "__main__":
    create_user("John Doe", "john@example.com")
    get_users()
    update_user(1, "John Smith", "johnsmith@example.com")
    delete_user(1)
            

            
