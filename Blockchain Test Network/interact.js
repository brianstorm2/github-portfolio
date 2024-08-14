const { Web3 } = require('web3');
const fs = require('fs');
const path = require('path');
const keythereum = require('keythereum');

// Initialize web3 with the provider pointing to your validator node
const web3 = new Web3('http://192.168.2.103:8550');

// Load account details
const accounts = {
  validator0: {
    address: '0x377dFC940D4e6A4ce446A34F0c26Ed94D831B6a7',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/validator0/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/validator0/password.txt'
  },
  validator1: {
    address: '0xC4580d4E2c3B2034f0Cc31bB01d6c5A149B679F0',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/validator1/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/validator1/password.txt'
  },
  validator2: {
    address: '0x35c700F5E24040E650ecfa828d1dA43df11f9E87',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/validator2/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/validator2/password.txt'
  },
  member0: {
    address: '0x0A1945626608B466207Bc29211727bA2f1b0386b',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member0/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member0/password.txt'
  },
  member1: {
    address: '0x493D571252572dAd4A945F947e6CF1eb3ee812A5',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member1/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member1/password.txt'
  },
  member2: {
    address: '0xB8aEd324409092eC8d481D89879769e28ca78ec8',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member2/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member2/password.txt'
  },
  member3: {
    address: '0xC7B7563808DB0f572bb91dD4342C065881676751',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member3/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member3/password.txt'
  },
  member4: {
    address: '0x8ABb86b06249E1d76122EA527d53fe6CE15405D2',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member4/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member4/password.txt'
  },
  member5: {
    address: '0xED3BB3D0650Cf69605F5AeafaF3652c80d710326',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member5/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member5/password.txt'
  },
  member6: {
    address: '0xAC049B521aa3C4D7050a0a763AEA4a7a35f3A368',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member6/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member6/password.txt'
  },
  member7: {
    address: '0xBe2742ff8463c72eeC6b99e583ca0AcA57c2072B',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member7/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member7/password.txt'
  },
  member8: {
    address: '0xE346a201AA96F2BDa8884326b8653ccc913BA3BA',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member8/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member8/password.txt'
  },
  member9: {
    address: '0xE800f3D126ea7df4A2e16c3eA05d3a054bbA6F2E',
    keystorePath: '/home/remnux/Documents/InvestBlockchain/member9/keystore/',
    passwordPath: '/home/remnux/Documents/InvestBlockchain/member9/password.txt'
  }
};

// Function to load private key
function loadPrivateKey(account) {
  const keystoreFile = fs.readdirSync(account.keystorePath).find(file => file.includes(account.address.slice(2).toLowerCase()));
  if (!keystoreFile) {
    throw new Error(`Keystore file for address ${account.address} not found`);
  }
  const keystoreContent = JSON.parse(fs.readFileSync(path.join(account.keystorePath, keystoreFile), 'utf8'));
  const password = fs.readFileSync(account.passwordPath, 'utf8').trim();
  return keythereum.recover(password, keystoreContent).toString('hex');
}

// Load the accounts
const loadedAccounts = {};
Object.keys(accounts).forEach(accountName => {
  const account = accounts[accountName];
  const privateKey = loadPrivateKey(account);
  const accountObj = web3.eth.accounts.privateKeyToAccount('0x' + privateKey);
  web3.eth.accounts.wallet.add(accountObj);
  loadedAccounts[accountName] = accountObj;
});

// Load ABIs from build artifacts
const identityArtifact = JSON.parse(fs.readFileSync('/home/remnux/Documents/InvestBlockchain/InvestContracts/build/contracts/IdentityVerification.json', 'utf8'));
const votingArtifact = JSON.parse(fs.readFileSync('/home/remnux/Documents/InvestBlockchain/InvestContracts/build/contracts/Voting.json', 'utf8'));

// ABI and address of the deployed IdentityVerification contract
const identityAbi = identityArtifact.abi;
const identityAddress = '0xf17b7dd93663Ea1b53498bC3Eb2c53A3344A2fe9'; // IdentityVerification contract address

// ABI and address of the deployed Voting contract
const votingAbi = votingArtifact.abi;
const votingAddress = '0x591A197A9aA26cDc59217ccA0FF2ac61B31967eD'; // Voting contract address

// Create contract instances
const identityContract = new web3.eth.Contract(identityAbi, identityAddress);
const votingContract = new web3.eth.Contract(votingAbi, votingAddress);

async function addValidator(validatorAddress) {
  try {
    const receipt = await identityContract.methods.addValidator(validatorAddress).send({
      from: loadedAccounts.validator0.address,
      gas: 2000000,
      gasPrice: '20000000000' // 20 Gwei
    });
    console.log('Validator added:', receipt);
  } catch (error) {
    console.error('Error adding validator:', error);
  }
}

async function verifyMember(memberAddress) {
  try {
    const receipt = await identityContract.methods.verifyMember(memberAddress).send({
      from: loadedAccounts.validator0.address,
      gas: 2000000,
      gasPrice: '20000000000' // 20 Gwei
    });
    console.log('Member verified:', receipt);
  } catch (error) {
    console.error('Error verifying member:', error);
  }
}

async function isMemberVerified(memberAddress) {
  try {
    const result = await identityContract.methods.isMemberVerified(memberAddress).call();
    console.log('Is member verified:', result);
    return result;
  } catch (error) {
    console.error('Error checking member verification status:', error);
  }
}

async function vote(business) {
  try {
    const receipt = await votingContract.methods.vote(business).send({
      from: loadedAccounts.member0.address,
      gas: 2000000,
      gasPrice: '20000000000' // 20 Gwei
    });
    console.log(`Voted for ${business}:`, receipt);
  } catch (error) {
    console.error('Error voting:', error);
  }
}

async function getVotes(business) {
  try {
    const votes = await votingContract.methods.getVotes(business).call();
    console.log(`Votes for ${business}:`, votes);
    return votes;
  } catch (error) {
    console.error('Error getting votes:', error);
  }
}

(async () => {
  const validatorAddress = '0x377dFC940D4e6A4ce446A34F0c26Ed94D831B6a7';
  await addValidator(validatorAddress);

  // Verify member address
  const memberAddress = '0x0A1945626608B466207Bc29211727bA2f1b0386b';
  await verifyMember(memberAddress);

  // Check if the member is verified
  await isMemberVerified(memberAddress);

  // Example usage for voting
  await vote('business0'); // Vote for business0
  await getVotes('business0'); // Get votes for business0
})();
