// setting up the dependencies

const electron = require("electron");
const url = require("url");
const path = require("path");

const {app,BrowserWindow} = electron;

let mainWindow;

// ok, so now listen for the app to be ready
