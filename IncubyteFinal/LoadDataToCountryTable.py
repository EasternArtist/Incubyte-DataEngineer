import pandas as pd
import sqlite3

countries = []

connection = sqlite3.connect('HospitalRecords.db')

c = connection.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
try:
    for row in c.fetchall():
        row = str(row).strip('\\()')
        row = str(row).strip(',')
        row = str(row).replace("'","")
        countries.append(row)
except sqlite3.Error as error:
    print("Failed to read data from table ", error)

countries = countries[1:]

c.execute('''
SELECT * FROM cust_details
          ''')

try:
    for row in c.fetchall():
        if "cust_{}".format(row[7]) in countries:
            print("cust_{}".format(row[7]))
            c.executemany("insert into cust_{} values(?,?,?,?,?,?,?,?,?,?);".format(row[7]),(row,))
        else:
            countries.append("cust_{}".format(row[7]))
            print("cust_{}".format(row[7]))
            c.execute("""create table cust_{}(name varchar(255) not null,cust_id varchar(18) not null,
            open_date date not null,consult_date date,vac_type char(5),
            dr_name char(255),state char(5),country char(5),
            dob date,cust_status char(1));""".format(row[7]))
            c.executemany("insert into cust_{} values(?,?,?,?,?,?,?,?,?,?);".format(row[7]),(row,))

except sqlite3.Error as error:
    print("Failed to read data from table", error)

connection.commit()
c.close()

