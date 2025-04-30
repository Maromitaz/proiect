const express = require('express');
const app = express();
const port = 3000;

const fs = require("fs");

app.get('/', (req, res) => {
    fs.readFile("./src/index.html", "utf-8", (err, data) => {
        if(err){
            console.error(err);
        }
        res.writeHead(200, {'content-type':'text/html'});
        res.write(data);
        return res.end();
    });

    // res.send('Hello World!');

})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
