import sqlite3 

# connecting to the database 
db_name="myTable.db"
db_delete=1
connection = sqlite3.connect(db_name) 

# cursor 
crsr = connection.cursor() 
sql_command = ""
#crsr.execute(sql_command)
while 1:

	lines = []
	while True:
    		line = input("Enter SQL line: ")
    		if line:
        		lines.append(line)
    		else:
        		break
	sql_command = '\n'.join(lines)
	print("sql_command:\n",sql_command,"\n--------\n")
	#sql_command=input("Enter SQL line: ")
	if sql_command=="-1":
		break
		db_delete=0
	if sql_command=="-2":
		db_delete=1
		break
	
	try:
		crsr.execute(sql_command)
		ans = crsr.fetchall() 
		print(ans) 
	except:
		print("sql_command error ")
	

connection.commit() 
try:
	crsr.execute("SELECT * FROM emp")  
	ans = crsr.fetchall()  
	print(ans)
except:
	print("no data")
connection.close() 
if db_delete:
	import os
	os.remove("myTable.db")
	


