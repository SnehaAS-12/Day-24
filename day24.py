#Create a JSON of all object types and import the JSON into a SQL Database

import json
college= [
    {"Name":"sneha","ID":12,"Section":"C","GPA":9.8,"GRADE":"O"},
    {"Name":"shahini","ID":22,"Section":"B","GPA":8.8,"GRADE":"A"},
    {"Name":"rohan","ID":24,"Section":"D","GPA":9.2,"GRADE":"O"}, 
    {"Name":"praveen","ID":14,"Section":"A","GPA":7.5,"GRADE":"B"}, 
    {"Name":"nandhini","ID":25,"Section":"C","GPA":8.2,"GRADE":"A"}
]
with open("college.json","w") as file:
    data= json.dump(college,file)
json_string = json.dumps(data)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Singapore@22",
    database="collegedb"
)
curr = mydb.cursor()
curr.execute("CREATE TABLE tutee(Name VARCHAR(30),ID int ,Section CHAR(10)),GPA int(5),GRADE VARCHAR(1)")
sql = "INSERT INTO tutee(Name,ID,Section,GPA,GRADE) VALUES (%s,%s,%s,%s,%s)"
values = json_string
curr.execute(sql,values)
mydb.commit()
curr.close()