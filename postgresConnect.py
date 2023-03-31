#30 March 2023
# postgresql driver program
# postgresConnect.py
# Requires the library
# pip install psycopg2

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="@Pass0rd@@@") 

  # create a cursor
cur = conn.cursor()

###########################################3
## gets the postgres version for testing
# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
##################################################


############################################


sqlCommand = """
create table IF NOT EXISTS employee(
    id serial primary key, 
    name varchar(50)
);
"""

cur.execute(sqlCommand)
conn.commit()

name = "dimitris"
sqlCommand = """
insert into  employee(  name ) values ('{}');
""".format(name)


cur.execute(sqlCommand)
conn.commit()



############################################
# close the communication with the PostgreSQL
cur.close()
