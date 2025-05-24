'use strict';
const fs = require("fs");
const path = require("path");

function readFileSyncAutoAlloc(path) {
  // Open file synchronously
  const fd = fs.openSync(path, 'r');

  try {
    // Get file size to auto allocate buffer
    const stats = fs.fstatSync(fd);
    const size = stats.size;

    // Allocate buffer automatically
    const buffer = Buffer.alloc(size);

    // Read whole file
    fs.readSync(fd, buffer, 0, size, 0);

    return buffer.toString('utf8');
  } finally {
    // Always close file descriptor
    fs.closeSync(fd);
  }
}

function renderTempalte(err, html, res) {

    var final_html = "";
    if (err) {
        console.error(err);
        if(res){
            return res.status(500).send("Internal server error.");
        }
    }
    var endLine = "\n";
    if (html.includes("\r\n"))
        endLine = "\r\n";
    const linii = html.split(endLine);
    for (let i = 0; i < linii.length; i++) {
        const linie = linii[i];
        if (linie.trim() !== '') {
            if (/{%.*?%}/.test(linie)) {
                const fisier = linie.match(/{%\s*(.*?)\s*%}/)[1].replace(/\s+/g, '');
                final_html += readFileSyncAutoAlloc(`./src/${fisier}`);
            } else if(/{!.*?!}/.test(linie)) {
                if(!res){
                    const fisier = linie.match(/{!\s*(.*?)\s*!}/)[1].replace(/\s+/g, '');
                    const css = path.join(`${__dirname}`, `..`, `/public${fisier}`);
                    final_html += `<link rel="stylesheet" href="${css}"></link>\n`;
                }else{
                    const fisier = linie.match(/{!\s*(.*?)\s*!}/)[1].replace(/\s+/g, '');
                    final_html += `<link rel="stylesheet" href="${fisier}"></link\n>`;
                }
            } else {
                final_html += `${linie}${endLine}`;
            }
        }
    }
    return final_html;
}

module.exports = {
    readFileSyncAutoAlloc,
    renderTempalte
}