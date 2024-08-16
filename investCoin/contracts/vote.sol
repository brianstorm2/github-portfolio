// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Vote {
    // each "vote" is 0.05 eth
    // Receive and fallback functions to handle incoming ETH
    receive() external payable {}

    fallback() external payable {}
}