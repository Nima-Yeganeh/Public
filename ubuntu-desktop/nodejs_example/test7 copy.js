const fs = require("fs");

// read a file
fs.readFile("input.txt", "utf-8", (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log("File contents:", data);
});

// write a file
fs.writeFile("output.txt", "Hello, world!", error => {
  if (error) {
    console.error(error);
    return;
  }
  console.log("File written successfully.");
});
