import pandas as pd
import sqlite3
from datetime import datetime

filename = "CustomerDetails.dsv"


data = pd.read_csv(filename,sep="|",skiprows = 1,header = None,usecols=range(2,12))

data.columns = ['name','cust_id','open_date','consult_date','vac_type','dr_name','state','country',
                'dob','cust_status']

try:    
    for i in range(len(data)) :
        row = data.loc[i, "open_date"] 
        row  = datetime.strptime(str(row),'%Y%m%d').date()
        data.loc[i,'open_date'] = row
    
    for i in range(len(data)) :
        row = data.loc[i, "consult_date"] 
        row  = datetime.strptime(str(row),'%Y%m%d').date()
        data.loc[i,'consult_date'] = row
    
    for i in range(len(data)) :
        row = data.loc[i, "dob"] 
        row  = datetime.strptime(str(row),'%d%m%Y').date()
        data.loc[i,'dob'] = row

except ValueError:
    pass

    
try:   
    connection = sqlite3.connect('HospitalRecords.db')
    
    c = connection.cursor()
    
    
    data.to_sql('cust_details', connection, if_exists='replace', index = False)
    
    
    c.execute('''
    SELECT * FROM cust_details
              ''')
    
    for row in c.fetchall():
        print (row)

except sqlite3.Error as error:
    print("Failed to load in table ", error)

finally:   
    c.close()
