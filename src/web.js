const express = require('express');
const app = express();
const fs = require("fs");
const port = 3000;
const renderTempalte = require('./main').renderTempalte

app.use(express.static('./public'));

app.get('/', (req, res) => {
    fs.readFile("./src/index.html", "utf-8", (err, html) => {
        res.writeHead(200, {'content-type':'text/html'});
        res.write(renderTempalte(err, html, res));
        return res.end();
    });
})

app.listen(port, () => {
    console.log(`Example app listening on port localhost:${port}`);
});
