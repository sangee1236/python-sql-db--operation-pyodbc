

#install using pip or any package manager
pip install pyodbc

#importing pyodbc  
import pyodbc

class Sql: 

 def __init__(self,server,database,username,password):
  self.connection_string = f"Driver={SQL Server};Server={server};Database={database};UID={username};PWD={password}"
   
 def sql_connection(self,query,operation): 
  connection = pyodbc.connect(self.connection_string)
  cursor = connection.cursor()
  cursor.execute(query)
  result = None
  try:
   if operation=="SELECT":
    result = cursor.fetchall()
   elif operation=="CUD_OPERATION":
    result = cursor.rowcount
    connection.commit()
  except Exception as ex:
    #Handle with care
      print(ex)
  finally:  
   connection.close()
  return result

#Select operation returns selected items
 def select_oper(self,query):
  Db = sqlcon() 
  result = Db.sqlcon(query,"SELECT")
  return result

#Create update or delete operations returns rows affected    
 def insert_update_delete_oper(self,query):
   Db = sqlcon()  
   result = Db.sqlcon(query,"CUD_OPERATION")
   return result

#Creating object for a class
obj = Sql(server,database,username,password)
result=obj.select_oper(query)
result_count=obj.insert_update_delete_oper(query)