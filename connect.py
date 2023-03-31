# 2023-03-23
# checks the connectivity with the database
# interacting with MS-SQL server

import pyodbc 

driver = 'DRIVER={SQL Server};'
server = 'SERVER=localhost,1433;' 
database = 'DATABASE=accBank;' 
username = 'UID=sa;' 
password = 'PWD=passw0rd;' 
trust = "TrustServerCertificate=True;" 

connectionString = driver+server+database+username+password+trust
 
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()