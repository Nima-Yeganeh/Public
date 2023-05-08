const express = require("express");

// create an express app
const app = express();

// define a route for GET requests to the root URL
app.get("/", (request, response) => {
  response.send("Hello, world!");
});

// define a route for GET requests to /users
app.get("/users", (request, response) => {
  const users = [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" },
    { id: 3, name: "Bob" },
  ];
  response.json(users);
});

// start the server
app.listen(8080, () => {
  console.log("Server is listening on port 8080...");
});
