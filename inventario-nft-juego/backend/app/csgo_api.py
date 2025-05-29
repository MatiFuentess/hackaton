import requests
from typing import List, Dict

BASE_URL = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en"

class CSGOApi:
    @staticmethod
    def get_all_items() -> Dict:
        """Obtener todos los items de CS:GO"""
        response = requests.get(f"{BASE_URL}/all.json")
        return response.json()
    
    @staticmethod
    def get_skins() -> List[Dict]:
        """Obtener todas las skins de CS:GO"""
        response = requests.get(f"{BASE_URL}/skins.json")
        return response.json()
    
    @staticmethod
    def get_stickers() -> List[Dict]:
        """Obtener todos los stickers de CS:GO"""
        response = requests.get(f"{BASE_URL}/stickers.json")
        return response.json()
    
    @staticmethod
    def get_agents() -> List[Dict]:
        """Obtener todos los agentes de CS:GO"""
        response = requests.get(f"{BASE_URL}/agents.json")
        return response.json()

    @staticmethod
    def format_item_for_nft(item: Dict) -> Dict:
        """Formatear un item de CS:GO para el formato NFT"""
        return {
            "name": item.get("name", "Unknown Item"),
            "description": item.get("description", ""),
            "image": item.get("image", ""),
            "attributes": [
                {
                    "trait_type": "Rarity",
                    "value": item.get("rarity", {}).get("name", "Common")
                },
                {
                    "trait_type": "Category",
                    "value": item.get("category", {}).get("name", "Miscellaneous")
                }
            ]
        } 