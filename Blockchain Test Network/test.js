const fs = require('fs');
const keythereum = require('keythereum');

// Define the path to your keystore file
const keystorePath = '/home/remnux/Documents/Geth/validator0/keystore/UTC--2024-05-06T19-33-17.547219400Z--4da2472edde765c406035c813912108955bdf33b';

// Define the password for your keystore file
const password = 'valid0';

// Read and decrypt the keystore file
const keystore = JSON.parse(fs.readFileSync(keystorePath, 'utf8'));
const privateKey = keythereum.recover(password, keystore).toString('hex');

console.log('Private Key:', privateKey);
