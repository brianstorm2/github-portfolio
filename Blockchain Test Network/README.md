This is the README of InvestBlockchain, a test network that facilitates P2P connections between 3 validators, 10 members and a bootnode, with smart contracts deployed to verify members and allow members to vote on potential investment opportunities

Requirements:
Geth v1.10.26
Node v16.0.0
Truffle

Script startup.sh is responsible for account creation and initialising accounts
- Accounts are created and a password creation function generates random passwords of 12 chars
- A textfile is created holding the account details for ease of examination. Encrypted using gpg. Run gpg accounts_info.txt.gpg and enter Password - account.info.unlock125
- Nodes have already been initialised

Script password-files.sh places a password textfile in each node directory, set to chmod 600 read only for account owner

A genesis.json file has been created to initialise the accounts created
-If the startup script is run again, a new genesis.json will have to be configured 

Script launchnodes.sh is responsible for initialising the nodes, setting up a listener at bootnode and initialising docker to run the accounts with SSL HTTPS
-If you want to run this script again, files chaindata and lightchaindata in /*node*/geth will need to be removed

Script startcontracts.sh is responsible for deploying smart contracts using Truffle
-identityverfication.sol is responsible for adding validators, and verifying members. 
-voting.sol is responsible for facilitating the voting system for members to vote on different organisations
-These contracts can be found in directory InvestContracts with other truffle configurations