// setting up the dependencies

const electron = require("electron");
const url = require("url");
const path = require("path");

const {app,BrowserWindow} = electron;

var ipc = require('electron').ipcMain;

let mainWindow;

// ok, so now listen for the app to be 

app.on('ready',function(){

    // now create window
    
    mainWindow = new BrowserWindow({});

    // load the html file to ble displayed

    mainWindow.loadURL(url.format({
        pathname : path.join(__dirname,'/src/main.html'),
        protocol : 'file' ,
        slashes : true
    }));

    // ok , so what this basically does is that it opens html in the created window (basically opens it as file://dirname/src/main.html) 
    // basic layout done



});

