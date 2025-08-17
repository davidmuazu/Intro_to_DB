import mysql.connector
from mysql.connector import Error   # Import Error 

try:
    # Try connecting to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",    
        password="Exclusive1@@@" 
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:  
    print(f"Error: {err}")

finally:
    # Always close connection safely
    if 'mydb' in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection closed.")
