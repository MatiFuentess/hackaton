from fastapi import APIRouter, HTTPException
from typing import List, Dict
from .csgo_api import CSGOApi

router = APIRouter()
csgo_api = CSGOApi()

# Mock data - replace with actual database
inventory = {}
nfts = {}
minted_items = {}

@router.get("/inventory/{wallet_address}")
async def get_inventory(wallet_address: str) -> Dict:
    if wallet_address not in inventory:
        inventory[wallet_address] = []
    return {"wallet": wallet_address, "items": inventory[wallet_address]}

@router.get("/nfts/{wallet_address}")
async def get_nfts(wallet_address: str) -> Dict:
    if wallet_address not in nfts:
        nfts[wallet_address] = []
    return {"wallet": wallet_address, "nfts": nfts[wallet_address]}

@router.get("/csgo/skins")
async def get_csgo_skins() -> List[Dict]:
    """Obtener todas las skins disponibles de CS:GO"""
    return csgo_api.get_skins()

@router.get("/csgo/stickers")
async def get_csgo_stickers() -> List[Dict]:
    """Obtener todos los stickers disponibles de CS:GO"""
    return csgo_api.get_stickers()

@router.get("/csgo/agents")
async def get_csgo_agents() -> List[Dict]:
    """Obtener todos los agentes disponibles de CS:GO"""
    return csgo_api.get_agents()

@router.post("/mint/csgo/{item_id}")
async def mint_csgo_item(item_id: str, wallet_address: str) -> Dict:
    """Mintear un item de CS:GO como NFT"""
    all_items = csgo_api.get_all_items()
    if item_id not in all_items:
        raise HTTPException(status_code=404, detail="Item not found")
        
    item = all_items[item_id]
    nft_metadata = csgo_api.format_item_for_nft(item)
    
    # Aquí iría la lógica de minteo real con blockchain
    if wallet_address not in minted_items:
        minted_items[wallet_address] = []
    minted_items[wallet_address].append(nft_metadata)
    
    return {
        "status": "success",
        "message": f"Item {item['name']} minted successfully",
        "metadata": nft_metadata
    }

@router.post("/inventory/{wallet_address}/add")
async def add_item(wallet_address: str, item_id: str):
    if wallet_address not in inventory:
        inventory[wallet_address] = []
    inventory[wallet_address].append(item_id)
    return {"status": "success", "message": f"Item {item_id} added to inventory"} 