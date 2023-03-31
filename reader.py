#23-3-2023

# read csv data from web or local csv
# inserts data in MSSQL server

import pandas as pd
import pyodbc as pc
from datetime import datetime, timedelta
import time


url = "https://stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"

df = pd.read_csv(url) 



driver = 'DRIVER={SQL Server};'
server = 'SERVER=localhost,1433;' 
database = 'DATABASE=accBank;' 
username = 'UID=sa;' 
password = 'PWD=passw0rd;' 
trust = "TrustServerCertificate=True;" 

connectionString = driver+server+database+username+password+trust
cnxn = pc.connect(connectionString, autocommit=True)    
cursor = cnxn.cursor()
start_time = time.time()
for index,row in df.iterrows():
    cursor.execute('INSERT INTO person([Name],price) values (?,?)', 
                    row['Variable_name'][0:50], 
                    row['Year'] )
    cnxn.commit()
cursor.close()
cnxn.close()

# see total time to do insert
print("%s seconds ---" % (time.time() - start_time))

print(df) 
print("program termination")

