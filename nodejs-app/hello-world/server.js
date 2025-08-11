const express = require('express');
const app = express();
const port = 3666;

app.get('/', (req, res) => {
  res.send('Hello from OpenShift on port 3666!');
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
