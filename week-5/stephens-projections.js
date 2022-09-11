// query to add a new user to the user's collection
db.users.insertOne({"firstName": 'Antonio', "lastName" : 'Vivaldi', "employeeId": '1013', "email": 'avivaldi@me.com', "dateCreated": new Date()}));

// query that updates Mozart's email address to mozart@me.com. Second, Write a query to prove the email address was updated
db.users.updateOne({"email": "wmozart@me.com"},{"$set":{"email": "mozart@me.com"}}));
db.users.findOne({"email": "mozart@me.com"}));

// query that lists all the documents in the user's collection. Only display the firstName, lastName, and email fields.
db.users.aggregate([{$project: {_id: 0,firstName: 1,lastName: 1,email: 1}}]));
