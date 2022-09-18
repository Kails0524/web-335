
#    Title: stephens_usersp1.py
#    Author: Kailee Stephens
#    Date: 09 18 2022
#    Description: Connect Python to MongoDB

# Import the MongoClient
from pymongo import MongoClient

# Connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@buwebdev-cluster-1.lsdxy.mongodb.net/?retryWrites=true&w=majority")

# Configure a variable to access the web335DB
db = client ['web335DB']

# Prints all users in collection
for user in db.users.find({}, {"firstName": 1, "lastName": 1 }):
    print(user)

# Prints employee info for person with ID number 1011
print(db.users.find_one({"employeeId":"1011"}))

# Prints employee info for person with last name Mozart
print(db.users.find_one({"lastName":"Mozart"}))
