const bcrypt = require("bcrypt");

// generate a salt to use for hashing
const saltRounds = 10;
const salt = bcrypt.genSaltSync(saltRounds);

// hash a password
const password = "my_password";
const hashedPassword = bcrypt.hashSync(password, salt);

console.log("Original password:", password);
console.log("Hashed password:", hashedPassword);

// compare a password to a hash
const isMatch = bcrypt.compareSync(password, hashedPassword);
console.log("Password matches hash:", isMatch);
