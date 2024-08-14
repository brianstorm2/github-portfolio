const HDWalletProvider = require('@truffle/hdwallet-provider');
const fs = require('fs');
const keythereum = require('keythereum');

// Define the path to your keystore and password files
const keystorePath = '/home/remnux/Documents/InvestBlockchain/validator0/keystore/';
const passwordPath = '/home/remnux/Documents/InvestBlockchain/validator0/password.txt';

// Read password
const password = fs.readFileSync(passwordPath, 'utf8').trim(); 

// Read and decrypt the keystore file
const keystoreFileName = fs.readdirSync(keystorePath)[0];
const keystore = JSON.parse(fs.readFileSync(`${keystorePath}${keystoreFileName}`, 'utf8'));
const privateKey = keythereum.recover(password, keystore).toString('hex');

module.exports = {
  networks: {
    development: {
      provider: () => new HDWalletProvider({
        privateKeys: [privateKey],
        providerOrUrl: 'http://192.168.2.103:8550', // Validator node's HTTP URL
        numberOfAddresses: 1,
      }),
      network_id: '*',
      gas: 4500000,
      gasPrice: 20000000000,
      networkCheckTimeout: 20000
    },
  },
  compilers: {
    solc: {
      version: "0.8.0",
    },
  },
};
