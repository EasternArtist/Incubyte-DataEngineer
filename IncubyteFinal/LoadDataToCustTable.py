import pandas as pd
import sqlite3

filename = "CustomerDetails.dsv"

data = pd.read_csv(filename,sep="|",skiprows = 1,header = None,usecols=range(2,12))

#print(data)

connection = sqlite3.connect('HospitalRecords.db')

c = connection.cursor()

data.to_sql('cust_details', connection, if_exists='replace', index = False)


c.execute('''
SELECT * FROM cust_details
          ''')

for row in c.fetchall():
    print (row)

c.close()