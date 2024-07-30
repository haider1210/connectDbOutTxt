import cx_Oracle,time,os
import sqlite3  

dsn_tns = cx_Oracle.makedsn('00.00.00.00', 1999, service_name='___') 
connection = cx_Oracle.connect(user='___', password='___', dsn=dsn_tns)

cursor_dev = connection_dev.cursor()
model_id=[.....................]
cursor_dev.execute(f'SELECT from table name  where model_id in {model_id}')
rows = cursor_dev.fetchall()

# for the printing the output
for  row in rows():
  print(row[0])

# for the storing the output in the text file
with open("testing.txt", "w") as f:
    for row in rows:
        f.write(f"{row[0]}\n")
        f.write("--------------------------------------------\n")
