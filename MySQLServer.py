import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="migbaru",
        password="migbaru@aastu"

        
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    
    mycursor.close()
    mydb.close()
    
except mysql.connector.Error as err:
    print(f"Error: {err}")