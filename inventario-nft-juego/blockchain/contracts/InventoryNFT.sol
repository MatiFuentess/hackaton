// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract InventoryNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    
    // Mapping from token ID to item type
    mapping(uint256 => string) private _itemTypes;
    
    constructor() ERC721("InventoryNFT", "INVT") {}
    
    function mintItem(address player, string memory tokenURI, string memory itemType)
        public
        onlyOwner
        returns (uint256)
    {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        
        _mint(player, newItemId);
        _setTokenURI(newItemId, tokenURI);
        _itemTypes[newItemId] = itemType;
        
        return newItemId;
    }
    
    function getItemType(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Item query for nonexistent token");
        return _itemTypes[tokenId];
    }
    
    function burn(uint256 tokenId) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "Caller is not owner nor approved");
        _burn(tokenId);
        delete _itemTypes[tokenId];
    }
} 