#!/bin/bash

# Start validator0 mining as they own the contract and need it for transactions
#docker exec -d validator0 geth --mine --miner.threads=1 --datadir /root/.ethereum --networkid 3129 --ipcpath /root/.ethereum/geth-validator0.ipc --unlock "0x377dFC940D4e6A4ce446A34F0c26Ed94D831B6a7" --password /root/.ethereum/password.txt --allow-insecure-unlock

# Wait for the mining to start
#sleep 10

# Navigate to the directory with the Truffle project
cd ~/Documents/InvestBlockchain/InvestContracts

# Compile the smart contracts
truffle compile

# Deploy and migrate the smart contracts
truffle migrate --network development

echo "Contracts deployed and migrated successfully."
