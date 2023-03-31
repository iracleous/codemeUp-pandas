# MongoDB driver application

# Mongodb document (JSON-style)
document_1 = {
  "_id" : "BF00001CFOOD",
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour"
}


from pymongo import MongoClient
 
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb//root@localhost:27017/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
 
# Access database
mydatabase = client['myData']
  
# Access collection of the database
mycollection=mydatabase['myTable']
  
# dictionary to be added in the database
record={
'title': 'MongoDB and Python', 
'description': 'MongoDB is no SQL database', 
'tags': ['mongodb', 'database', 'NoSQL'], 
'viewers': 104 
}
  
# inserting the data in the database
rec = mydatabase.myTable.insert(record)