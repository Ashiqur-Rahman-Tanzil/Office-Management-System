"""
This program will show all posted notices in our Office Management System.
There are four functions to group them for the user help.
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
DB_PASS = "1234" # password for database currently ommited.


conn = psycopg2.connect(dbname=DB_NAME , user= DB_USER , password= DB_PASS , host= DB_HOST) #connecting declared database with "conn" variable via psycopg2.

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #connecting the cursor.

app = Flask(__name__)
@app.route('/')



def allNotices(): 
    """
    shows all notices form the database and renders to Office Management System's Notice Board page.
    
    """
    cursor.execute("select notice_body from notice_board ;") #geetting data via sql command in cursor from the database.
    all_notices = cursor.fetchall() #fetching all data from cursor.
    #"print(all_notices)" printing to check it on terminal. This line was created for testing purpose.
    return render_template("notice_board.html" , notices = all_notices) #returning to template page.
    #"return all_notices" This line was created for testing purpose.
def groupByDate(): 
    """        
    groups all the notices by present date and shows notices posted today.
    
    """
    cursor.execute("select notice_body from notice_board where post_date = CURRENT_DATE;") #geetting data via sql command in cursor from the database.
    todays_notices = cursor.fetchall() #fetching all data from cursor.
    #"print(todays_notices)" printing to check it on terminal. This line was created for testing purpose.
    return render_template("notice_board.html" , notices= todays_notices) #returning to template page.
    #"return todays_notices" This line was created for testing purpose.

def groupByDept(dpt): 
    """
    groups notices by department and shows selected notices.
    :type dpt: string
    :param dpt: desired department name to see department associated notices.
    
    """
    query = "select notice_body from notice_board where dept_id = " +dpt+" ;"
    cursor.execute(query) #geetting data via sql command in cursor from the database.
    dept_notices = cursor.fetchall() #fetching all data from cursor.
    #"print(dept_notices)" printing to check it on terminal. This line was created for testing purpose.
    return render_template("notice_board.html" , notices= dept_notices) #returning to template page.
    #"return dept_notices"  This line was created for testing purpose.


def groupByPriority(pt): 
    """
    groups notices by their priority level and shows them.
    :type pt: string
    :param pt: desired priority level to see associated notices.

    """

    query = "select notice_body from notice_board where priority_level ="+ pt +";"
    cursor.execute(query) #geetting data via sql command in cursor from the database.
    priority_notices = cursor.fetchall() #fetching all data from cursor.
    #"print(priority_notices)" printing to check it on terminal. This line was created for testing purpose.
    return render_template("notice_board.html" , notices= priority_notices) #returning to template page.
    #"return priority_notices" This line was created for testing purpose.





#this main finction was also created for testing purpose
#def main(): 
    #allNotices()
    #groupByDate()
    #groupByDept('333')
    #groupByPriority('5')  

#if __name__ == "__main__":
   # main()



conn.commit() #commiting to trace redundancy
cursor.close() #closing cursor
conn.close() #closing connection with database