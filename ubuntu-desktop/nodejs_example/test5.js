const nodemailer = require("nodemailer");

// create reusable transporter object using the default SMTP transport
let transporter = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 465,
  secure: true, // use SSL
  auth: {
    user: "your-email@gmail.com",
    pass: "your-email-password",
  },
});

// setup email data with unicode symbols
let mailOptions = {
  from: '"Sender Name" <your-email@gmail.com>', // sender address
  to: "recipient-email@example.com", // list of receivers
  subject: "Hello from Node.js", // Subject line
  text: "Hello world?", // plain text body
  html: "<b>Hello world?</b>", // html body
};

// send mail with defined transport object
transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    return console.log(error);
  }
  console.log("Message sent: %s", info.messageId);
});
