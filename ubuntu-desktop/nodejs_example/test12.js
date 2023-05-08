const { exec } = require("child_process");

// execute an Ubuntu administration command
exec("sudo apt-get update", (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Error: ${stderr}`);
    return;
  }
  console.log(`Output: ${stdout}`);
});
