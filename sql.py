import pyodbc 

server = 'server_name' 
database = 'database' 
username = 'myusername' 
password = 'mypassword' 
connection = pyodbc.connect(f'DRIVER={ODBC Driver 17 for SQL Server};SERVER={server}DATABASE={database};UID=username};PWD={password}')

#cursor is a object represents a database cursor
cursor = connection.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
#To fetch single record 
row = cursor.fetchone() 
#To fetch all record 
rows = cursor.fetchall() 

#Loop for single and multiple select 
for row in rows:
	print(row)

while row: 
    print row[0] 
    row = cursor.fetchone()


#Sample insert, update delete query
#execute a statement
cursor.execute("Insert,update, delete statements") 
#fetch single inserted record  
row = cursor.fetchone()

# Commits all executed statements
connection.commit()

#RollBack or reverts all executed statements
connection.rollback()

#Get rowcount on update and delete
row = cursor.rowcount
print(row_count)