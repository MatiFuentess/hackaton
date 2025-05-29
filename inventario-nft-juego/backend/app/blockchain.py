from web3 import Web3
from eth_account import Account
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to local node or infura
INFURA_URL = os.getenv("INFURA_URL", "http://localhost:8545")
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def connect_wallet(private_key: str) -> str:
    """Connect a wallet using private key"""
    account = Account.from_key(private_key)
    return account.address

def get_nft_balance(wallet_address: str, contract_address: str) -> int:
    """Get NFT balance for a wallet"""
    # Add your NFT contract ABI here
    contract_abi = []
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    return contract.functions.balanceOf(wallet_address).call()

def mint_nft(wallet_address: str, token_uri: str) -> str:
    """Mint a new NFT"""
    # Add your minting logic here
    return "NFT minted successfully" 