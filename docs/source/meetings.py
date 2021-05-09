"""
This program will show the meeting schedules in our Office Management System.
Author: Ashiqur Rahman
ID: 1712389642

"""


from flask import Flask
from flask import render_template # Renders to tmeplates.
import psycopg2
import psycopg2.extras

DB_NAME = "officemanagementsystem" #database name.
DB_HOST = "localhost" # host for database here "localhost".
DB_USER = "postgres" #username for database here default "postgres".
DB_PASS = "1234" # password for database. Currently ommited.


conn = psycopg2.connect(dbname=DB_NAME , user= DB_USER , password= DB_PASS , host= DB_HOST) #connecting declared database with "conn" variable via psycopg2.

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #connecting the cursor.

app = Flask(__name__)
@app.route('/')


def showMeetings():
    """
    fetches the meeting schedules from the database and renders to Office Management System's meeting page.
    
    """

    cursor.execute("select meeting_body from meetings ;") #geetting data via sql command in cursor from the database.
    all_meetings = cursor.fetchall() #fetching all data from cursor.
    return render_template("meetings.html" , meetings = all_meetings) #returning to template page.
    # "return all_meetings #print(all_meetings)" these lines were created for testing purpose.



#def main(): this main finction was also created for testing purpose
    #showMeetings()

#if __name__ == "__main__":
   # main()


conn.commit() #commiting to trace redundancy
cursor.close() #closing cursor
conn.close() #closing connection with database