import pandas as pd
import sqlite3

countries = []

connection = sqlite3.connect('HospitalRecords.db')

c = connection.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
try:
    for row in c.fetchall():
        countries.append(row[0])
except sqlite3.Error as error:
    print("Failed to read data from table | ", error)

print(countries)
c.execute('''
SELECT * FROM cust_details
          ''')
          
def insertInTheTable(row):
    c.executemany("insert into cust_{} values(?,?,?,?,?,?,?,?,?,?);".format(row[7]),(row,))

try:
    for row in c.fetchall():
        if "cust_{}".format(row[7]) in countries:
            insertInTheTable(row)
        else:
            countries.append("cust_{}".format(row[7]))
            print("Table Created : ","cust_{}".format(row[7]))
            c.execute("""create table cust_{}(name varchar(255) not null,cust_id varchar(18) primary key,
            open_date date not null,consult_date date,vac_type char(5),
            dr_name char(255),state char(5),country char(5),
            dob date,cust_status char(1));""".format(row[7]))
            insertInTheTable(row)

except sqlite3.Error as error:
    print("Failed to load data in table |", error)

finally:
    connection.commit()
    c.close()

