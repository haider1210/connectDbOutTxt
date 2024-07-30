import cx_Oracle,time,os

dsn_tns = cx_Oracle.makedsn('00.00.00.00', 1999, service_name='___') 
connection = cx_Oracle.connect(user='___', password='___', dsn=dsn_tns)

cursor_dev = connection_dev.cursor()
model_id=[.....................]
cursor_dev.execute(f'SELECT from table name  where model_id in {model_id}')
rows = cursor_dev.fetchall()
for  row in rows():
  print(row[0])
