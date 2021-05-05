"""
This program will manage the user login authentication in our Office Management System.
Author: Ashiqur Rahman
ID: 1712389642
"""



from flask import Flask
from flask import render_template # Renders to tmeplates.
import psycopg2
import psycopg2.extras



DB_NAME = "officemanagementsystem" #database name
DB_HOST = "localhost" # host for database here "localhost".
DB_USER = "postgres" #username for database here default "postgres".
DB_PASS = "1234" # password for database currently ommited.



conn = psycopg2.connect(dbname=DB_NAME , user= DB_USER , password= DB_PASS , host= DB_HOST) #connecting declared database with "conn" variable via psycopg2.

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #connecting the cursor.

app = Flask(__name__)
@app.route('/' , methods= ["GET", "POST"])

def checkLogin(): 
    """
    verify the user login informations from login page form.
    
    """

    if request.method == "POST": 
        id = request.form.get(id) #getting id from  html form into id variable.
        passw= request.form.get(pwd) #getting password from html form.
        cursor.execute("select id from user_list ;") #fetching id's from database.
        db_id = cursor.fetchall() 
        if id == db_id: #checks if a valid id is provided or not.
            cursor.execute("select user_password from user_list ;") #fetch password for the id from database.
            db_pass = cursor.fetchall()
            if db_pass == passw: #checks password's validity.
                return redirect('home.html') #if valid, redirecting to home page.
            else: # if id or password is invalid then redirecting to login page again with a message.
                msg = "invalid id or password"
                return render_template("login.html" , msg = msg)
        else: # if id or password is invalid then redirecting to login page again with a message.
            msg = "invalid id or password"
            return render_template("login.html" , msg = msg)





conn.commit() #commiting to trace redundancy
cursor.close() #closing cursor
conn.close() #closing connection with database
