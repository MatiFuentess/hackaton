// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract GameItems {
    string public name = "Game Items";
    
    struct Item {
        uint256 id;
        string name;
        string description;
    }
    
    mapping(uint256 => Item) public items;
    uint256 public nextItemId;
    
    event ItemCreated(uint256 indexed id, string name, string description);
    
    function createItem(string memory _name, string memory _description) public {
        uint256 itemId = nextItemId;
        items[itemId] = Item(itemId, _name, _description);
        nextItemId++;
        
        emit ItemCreated(itemId, _name, _description);
    }
} 