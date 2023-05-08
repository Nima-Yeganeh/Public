const jwt = require("jsonwebtoken");

// generate a JWT
const user = { id: 123 };
const secret = "my_secret_key";
const token = jwt.sign(user, secret);

console.log("Token:", token);

// verify a JWT
jwt.verify(token, secret, (error, decoded) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log("Decoded token:", decoded);
});
