const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const InventoryNFT = await ethers.getContractFactory("InventoryNFT");
  const inventoryNFT = await InventoryNFT.deploy();

  await inventoryNFT.deployed();

  console.log("InventoryNFT deployed to:", inventoryNFT.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  }); 