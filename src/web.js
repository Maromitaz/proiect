const express = require('express');
const app = express();
const port = 3000;
const main = require('./main')
console.log(main)

app.use(express.static('./public'));

const fs = require("fs");

app.get('/', (req, res) => {
    fs.readFile("./src/index.html", "utf-8", (err, data) => {
        if(err){
            console.error(err);
            return res.status(500).send("Internal server error.");
        }
        res.writeHead(200, {'content-type':'text/html'});
        res.write(data);
        return res.end();
    });
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
