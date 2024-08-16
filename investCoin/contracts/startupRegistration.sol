// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract startupRegistration {
    //account initialisation for startups
    struct startupAccount {
        address payable startupAddress;
        string accountName;
        bool registered;
        //uint256 registrationFee;
    }

    mapping (address => startupAccount) startups;
    //require registration fee
}
