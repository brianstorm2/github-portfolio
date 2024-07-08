#!/bin/bash

# Define base directory
BASE_DIR=~/Documents/InvestBlockchain

# Define nodes and their passwords
declare -A NODES=(
    ["bootnode"]="ewwKceQ49b6J"
    ["validator0"]="2yuZRH8DF9WZ"
    ["validator1"]="NE9SGJHj1mPP"
    ["validator2"]="s6YhgBN69dpf"
    ["member0"]="1gsZWCV7vIVV"
    ["member1"]="DeVlvgTG2baE"
    ["member2"]="OCRKZAbg17cf"
    ["member3"]="8UzaJbvhHWJK"
    ["member4"]="NdeiY8s3I8zF"
    ["member5"]="8gr7XzgQbs2U"
    ["member6"]="4BMmzQiI0YAX"
    ["member7"]="eg9gmfMJr7OJ"
    ["member8"]="iZjDxR91EYns"
    ["member9"]="xKUErBCFOUYa"
)

# Create password files and set permissions
for NODE in "${!NODES[@]}"; do
    PASSWORD="${NODES[$NODE]}"
    PASSWORD_FILE="$BASE_DIR/$NODE/password.txt"

    # Create the password file
    echo "$PASSWORD" > "$PASSWORD_FILE"

    # Set the file permissions
    chmod 600 "$PASSWORD_FILE"

    echo "Password file created and secured for $NODE"
done

echo "All password files have been created and secured."
