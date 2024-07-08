#!/bin/bash

# Define base directories
BASE_DIR=~/Documents/InvestBlockchain
GENESIS_FILE=$BASE_DIR/genesis.json
BOOTNODE_DIR=$BASE_DIR/bootnode

# Define the bootnode enode address
BOOTNODE_ENODE="enode://7e7505f2e77bf4d8ca684fb1f497910cddf8d5e4275ab6518c89ea8c367d08da8045562d72c90dc7c19957d7e7be845735a6456166a16c1a6f0bf77339a50b46@192.168.0.223:30305"

# Initialise the bootnode
geth init --datadir $BOOTNODE_DIR $GENESIS_FILE

# Start the bootnode
sudo geth --datadir $BOOTNODE_DIR --networkid 3129 --port 30305 --ipcpath geth-bootstrap.ipc --http --http.addr "0.0.0.0" --http.port 8545 --http.api "admin,eth,net,web3,personal,miner" --http.corsdomain "*" --http.vhosts "*" --netrestrict '192.168.0.223'

# Initialise and run validator nodes
for i in {0..2}; do
    VALIDATOR_DIR=$BASE_DIR/validator$i
    HTTP_PORT=$((8550 + 2 * i))
    IPC_PORT=$((30306 + i))
    PASSWORD_FILE=$VALIDATOR_DIR/password.txt

    # Initialise the validator
    docker run --rm -v $BASE_DIR:/Documents/InvestBlockchain -v $VALIDATOR_DIR:/root/.ethereum ethereum/client-go:alltools-v1.10.26 geth init /Documents/InvestBlockchain/genesis.json

    # Run the validator
    docker run -d --name validator$i -v $VALIDATOR_DIR:/root/.ethereum -p $HTTP_PORT:$HTTP_PORT -p $IPC_PORT:$IPC_PORT ethereum/client-go:alltools-v1.10.26 geth --datadir /root/.ethereum --networkid 3129 --ipcpath /root/.ethereum/geth-validator$i.ipc --bootnodes $BOOTNODE_ENODE --syncmode "full" --http --http.addr "0.0.0.0" --http.port $HTTP_PORT --http.api "admin,eth,net,web3,personal,miner" --allow-insecure-unlock --mine --miner.threads=1 --unlock 0 --password /root/.ethereum/password.txt
done

# Initialise and run member nodes
for i in {0..9}; do
    MEMBER_DIR=$BASE_DIR/member$i
    HTTP_PORT=$((8535 + i))
    IPC_PORT=$((30295 + i))
    PASSWORD_FILE=$MEMBER_DIR/password.txt

    # Initialize the member
    docker run --rm -v $BASE_DIR:/Documents/InvestBlockchain -v $MEMBER_DIR:/root/.ethereum ethereum/client-go:alltools-v1.10.26 geth init /Documents/InvestBlockchain/genesis.json

    # Run the member
    docker run -d --name member$i -v $MEMBER_DIR:/root/.ethereum -p $HTTP_PORT:$HTTP_PORT -p $IPC_PORT:$IPC_PORT ethereum/client-go:alltools-v1.10.26 geth --datadir /root/.ethereum --networkid 3129 --ipcpath /root/.ethereum/geth-member$i.ipc --bootnodes $BOOTNODE_ENODE --syncmode "full" --http --http.addr "0.0.0.0" --http.port $HTTP_PORT --http.api "admin,eth,net,web3,personal" --allow-insecure-unlock --unlock 0 --password /root/.ethereum/password.txt
done

echo "Initialisation and launch complete."
