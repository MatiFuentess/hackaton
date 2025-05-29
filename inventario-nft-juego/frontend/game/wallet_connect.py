import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class WalletConnect:
    def __init__(self):
        self.api_url = os.getenv("API_URL", "http://localhost:8000")
        self.wallet_address = None
        self.connected = False
        
    def connect(self, wallet_address: str) -> bool:
        """Connect to a wallet"""
        try:
            response = requests.get(f"{self.api_url}/inventory/{wallet_address}")
            if response.status_code == 200:
                self.wallet_address = wallet_address
                self.connected = True
                return True
        except requests.RequestException:
            pass
        return False
        
    def get_inventory(self) -> list:
        """Get inventory items for connected wallet"""
        if not self.connected:
            return []
            
        try:
            response = requests.get(f"{self.api_url}/inventory/{self.wallet_address}")
            if response.status_code == 200:
                return response.json().get("items", [])
        except requests.RequestException:
            pass
        return []
        
    def get_nfts(self) -> list:
        """Get NFTs for connected wallet"""
        if not self.connected:
            return []
            
        try:
            response = requests.get(f"{self.api_url}/nfts/{self.wallet_address}")
            if response.status_code == 200:
                return response.json().get("nfts", [])
        except requests.RequestException:
            pass
        return [] 