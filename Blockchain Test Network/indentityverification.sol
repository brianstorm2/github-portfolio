// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IdentityVerification {
    address public owner;
    mapping(address => bool) public validators;
    mapping(address => bool) public verifiedMembers;

    event MemberVerified(address member);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyValidator() {
        require(validators[msg.sender], "Only validators can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function addValidator(address _validator) public onlyOwner {
        validators[_validator] = true;
    }

    function verifyMember(address _member) public onlyValidator {
        verifiedMembers[_member] = true;
        emit MemberVerified(_member);
    }

    function isMemberVerified(address _member) public view returns (bool) {
        return verifiedMembers[_member];
    }
}
