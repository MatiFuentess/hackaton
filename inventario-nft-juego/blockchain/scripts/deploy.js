const { ethers } = require("hardhat");

async function main() {
  const GameItems = await ethers.getContractFactory("GameItems");
  const gameItems = await GameItems.deploy();
  await gameItems.deployed();

  console.log("GameItems deployed to:", gameItems.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  }); 