/**
 * Title: MongoDB Shell 
 * Author: Kailee Stephens 
 * Date: 09/04/2022
 * Description: queries for MongoDB Shell
 */

//locates all documents in the user's collection
db.users.find();

//locates email address of jBach

db.users.find( { email: "jbach@me.com" } );

//locates last name of Mozart

db.users.find( { lastName: "Mozart" } );

//locates first name of Richard

db.users.find( { firstName: "Richard" } );

//locates employeeId of 1010

db.users.find( { employeeId: "1010" } );
