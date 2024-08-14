// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    address public owner;
    mapping(address => bool) public members;
    mapping(string => uint256) public votes;
    string[] public businesses;

    event Voted(address indexed member, string business, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only members can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
        businesses.push("business0");
        businesses.push("business1");
        businesses.push("business2");
    }

    function addMember(address _member) public onlyOwner {
        members[_member] = true;
    }

    function vote(string memory business) public payable onlyMember {
        require(isValidBusiness(business), "Invalid business");
        require(msg.value > 0, "You need to send some Ether to vote");
        votes[business] += msg.value;
        emit Voted(msg.sender, business, msg.value);
    }

    function getVotes(string memory business) public view returns (uint256) {
        return votes[business];
    }

    function withdraw() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    function isValidBusiness(string memory business) internal view returns (bool) {
        for (uint256 i = 0; i < businesses.length; i++) {
            if (keccak256(abi.encodePacked(businesses[i])) == keccak256(abi.encodePacked(business))) {
                return true;
            }
        }
        return false;
    }
}
