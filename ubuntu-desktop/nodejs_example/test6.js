const mongoose = require("mongoose");

// connect to the database
mongoose.connect("mongodb://localhost/myapp", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => {
    console.log("Connected to database.");
    
    // define a schema for the data
    const personSchema = new mongoose.Schema({
      name: String,
      age: Number,
    });

    // define a model for the data
    const Person = mongoose.model("Person", personSchema);

    // create a new person
    const john = new Person({
      name: "John",
      age: 30,
    });

    // save the person to the database
    john.save()
      .then(() => {
        console.log("Person saved to database.");
        
        // find all people in the database
        Person.find()
          .then(people => {
            console.log("All people in database:", people);
            
            // update the person's age
            john.age = 31;
            john.save()
              .then(() => {
                console.log("Person updated in database.");

                // delete the person from the database
                john.delete()
                  .then(() => {
                    console.log("Person deleted from database.");
                  })
                  .catch(error => {
                    console.error(error);
                  });
              })
              .catch(error => {
                console.error(error);
              });
          })
          .catch(error => {
            console.error(error);
          });
      })
      .catch(error => {
        console.error(error);
      });
  })
  .catch(error => {
    console.error(error);
  });
  