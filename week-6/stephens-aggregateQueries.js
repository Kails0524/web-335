// query that shows a list of documents in the houses collection
db.houses.find();

// query that shows a list of documents in the student's collection
db.students.find();

//query to add a document to the student’s collection.  
db.students.insertOne({ "firstName": 'Harry', "lastName": 'Potter', "studentId": 's1010', "houseId": 'h1007'});
db.students.find({ "lastName": "Potter" });

// query that deletes the document added above and write a query to prove the document was deleted
db.students.deleteOne({ "studentId": "s1019" });
db.students.find({ "lastName": "Potter" });

//query to show a list of students by house 
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            as: "house"
        }
    }
]);

//query to show a list of students for house Gryffindor 
db.students.aggregate([
    {
        $lookup: {
            from: "houses",
            localField: "houseId",
            foreignField: "houseId",
            pipeline: [
                {
                    $match: {
                        houseId: "h1008"
                    }
                }
            ],
            as: "house"
        },
    }
]);

//query to show a list of students for the Eagle mascot 
db.students.aggregate([
    {
        $lookup: {
            from: "houses", // foreign collection (houses)
            as: "houseMascot", // output array field 
            let: { houseId: "$houseId" }, // expression
            pipeline: [
                {
                    $match: {
                        $expr: {
                            $and: [
                                { $eq: ["$houseId", "$$houseId"] }, 
                                { $eq: ["$mascot", "Eagle"] }
                            ]
                        }
                    }
                }
            ],
        }
    }
]);
