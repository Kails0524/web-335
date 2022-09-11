/**
 * Title: Projections
 * Author: Kailee Stephens 
 * Date: 09/11/2022
 */

// query to add a new user 
db.users.insertOne({"firstName": 'Antonio', "lastName" : 'Vivaldi', "employeeId": '1013', "email": 'avivaldi@me.com', "dateCreated": new Date()}));

// query that updates Mozart's email address 
db.users.updateOne({"email": "wmozart@me.com"},{"$set":{"email": "mozart@me.com"}}));

//query to prove the email address was updated
db.users.findOne({"email": "mozart@me.com"}));

// query that lists all the documents, displaying only the firstName, lastName, and email fields.
db.users.aggregate([{$project: {_id: 0,firstName: 1,lastName: 1,email: 1}}]));
