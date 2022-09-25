#    Title: stephens_usersp2.py
#    Author: Kailee Stephens
#    Date: 09 25 2022
#    Description: Python with MongoDB pt2

# import MongoDB client
from pymongo import MongoClient
import datetime


# string from MongoDB for to connect to database
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.lsdxy.mongodb.net/?retryWrites=true&w=majority")

# variable for accessing the web335 database
db = client['web33DB']

# create new user document
john = {
    "firstName": "John",
    "lastName": "Williams",
    "employeeId": "1018",
    "email": "jwilliams@me.com",
}

# insert new user into database
db.users.insertOne(john)

# print newly added document
print(db.users.find( { "employeeId": "1018" } ))

# update newly added document's email field
db.users.update(
    { "employeeId": "1018" },
    {    "$set": {
            "email": "john.williams@me.com"
        }
    }
)

# print updated document 
print(db.users.find( { "employeeId": "1018" } ))

# delete the new document from the database
db.users.deleteOne( { "employeeId": "1018" } )

# try finding deleted document to check that it was deleted
print(db.users.find( { "employeeId": "1018" } ))
