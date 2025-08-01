const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from OpenShift on port 3000!');
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
