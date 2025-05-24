const { app, BrowserWindow } = require('electron');
const fs = require("fs");
const renderTempalte = require('./main').renderTempalte

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600
    });

    // win.loadFile('index.html');
    fs.readFile("./src/index.html", "utf-8", (err, html) => {
        const lafrance = renderTempalte(err, html, 0);
        console.log(lafrance);
        win.loadURL(`data:text/html;charset=utf-8,${lafrance}`)
    });
    
}

app.commandLine.appendSwitch('gtk-version', '3');

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});
