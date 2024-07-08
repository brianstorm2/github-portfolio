#!/bin/bash

# Define base directory
BASE_DIR=~/Documents/InvestBlockchain
INFO_FILE=$BASE_DIR/accounts_info.txt

# Clear previous info file
echo -n "" > $INFO_FILE

# Function to generate a random password
generate_password() {
    local PASSWORD_LENGTH=12
    local PASSWORD=$(< /dev/urandom tr -dc 'A-Za-z0-9' | head -c${1:-$PASSWORD_LENGTH})
    echo $PASSWORD
}

# Function to create a new account and log info
create_account() {
    local ACCOUNT_NAME=$1
    local PASSWORD=$(generate_password)

    # Create a new account and capture the output
    local ACCOUNT_OUTPUT=$(echo $PASSWORD | geth account new --password <(echo $PASSWORD) --datadir $BASE_DIR/$ACCOUNT_NAME 2>&1)

    # Extract the public key and path to the keystore file
    local PUBLIC_KEY=$(echo "$ACCOUNT_OUTPUT" | grep -oP '(?<=Public address of the key:   ).*')
    local KEYSTORE_PATH=$(echo "$BASE_DIR/$ACCOUNT_NAME/keystore/UTC--.*--$PUBLIC_KEY")

    # Log account information
    echo "Node Name: $ACCOUNT_NAME" >> $INFO_FILE
    echo "Password: $PASSWORD" >> $INFO_FILE
    echo "Public Key: $PUBLIC_KEY" >> $INFO_FILE
    echo "Path to Private Key: $KEYSTORE_PATH" >> $INFO_FILE
    echo "" >> $INFO_FILE
}

# Create the bootnode account
create_account "bootnode"

# Create validator accounts
for i in {0..2}; do
    create_account "validator$i"
done

# Create member accounts
for i in {0..9}; do
    create_account "member$i"
done

echo "Account creation complete. Information saved to $INFO_FILE"
