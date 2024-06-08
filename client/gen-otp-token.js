// Test with: node client/run.js
// Deploy in Scriptable App to run on iOS

// Uncommented lines to run with Node.js

// const { sha3_256 } = require('./js-sha3');
const sha3_256 = importModule('js-sha3');

const SALT = '<your-secret-salt>';

const timestamp = Math.floor(Math.floor(Date.now() / 1000) / 30) * 30;

function generateHash(salt, timestamp) {
    return sha3_256(salt + timestamp.toString());
}

const token = generateHash(SALT, timestamp);

Script.setShortcutOutput(token);
Script.complete();
