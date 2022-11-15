#!pip install mysql-connector-python
import mysql.connector as conn
mydb = conn.connect(host = 'localhost',user = 'root' ,passwd = "root")
cursor = mydb.cursor()
cursor.execute("show databases")
cursor.fetchall()
cursor.execute('use test_gunjan')
#cursor.execute('create table test_g(studentid INT(10) ,firstname VARCHAR(30)  ,lastname VARCHAR(30) ,regid INT(10) ,classname VARCHAR(30))')

cursor.execute('show tables')
cursor.fetchall()
cursor.execute('insert into test_g values(423424 , "Ram" , "kumar" , 2344323 , "FSDS1")')
mydb.commit()
cursor.execute("select * from test_g")
cursor.fetchall()
cursor.execute('show tables')
#Bulk upload
#cursor.execute('create table test_gunjan.glass(col1 INT(10) ,col2 float(10,5),col3 float(10,5) ,col4 float(10,5) , col5 float(10,5),col6 float(10,5),col7 float(10,5),col8 float(10,5), col9 float(10,5), col10 float(10,5), col11 int(10)) ')

file = open("glass.data", 'r')
file.read()

import csv
with open('glass.data', 'r') as f:
    glass_data = csv.reader(f, delimiter = '\n')
    #print(glass_data)
    for i in glass_data:
        print(i)

#cursor.execute('create table test_gunjan.glass(col1 INT(10) ,col2 float(10,5),col3 float(10,5) ,col4 float(10,5) , col5 float(10,5),col6 float(10,5),col7 float(10,5),col8 float(10,5), col9 float(10,5), col10 float(10,5), col11 int(10))')

cursor.execute('insert into glass values(1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)')
mydb.commit()
cursor.execute("select * from glass")
cursor.fetchall()

with open('glass.data','r') as f:
    glass_data=csv.reader(f,delimiter='\n')
    for i in glass_data:
        print(type(i[0]))
        print(f'insert into glass values ({str(i[0])})')
        cursor.execute('insert into glass values({values})'.format(values = ((i[0]))))

mydb.commit()

cursor.execute('show tables')
cursor.fetchall()

import pandas as pd
pd.read_sql("select * from glass" , mydb)
pd.read_sql("show databases", mydb)
