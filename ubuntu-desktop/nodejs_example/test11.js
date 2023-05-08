const axios = require("axios");

// make a GET request to an API
axios.get("https://jsonplaceholder.typicode.com/posts")
  .then(response => {
    console.log("API response:", response.data);
  })
  .catch(error => {
    console.error(error);
  });

// make a POST request to an API
axios.post("https://jsonplaceholder.typicode.com/posts", {
    title: "My Post",
    body: "This is my post.",
    userId: 1
  })
  .then(response => {
    console.log("API response:", response.data);
  })
  .catch(error => {
    console.error(error);
  });
  