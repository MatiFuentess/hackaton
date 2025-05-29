# NFT Inventory Game

A blockchain-based game where players can collect, trade, and use NFT items in their inventory.

## Project Structure

```
inventario-nft-juego/
├── backend/          # FastAPI backend server
├── frontend/         # Pygame-based game client
├── blockchain/       # Smart contracts and deployment
├── ipfs/            # IPFS metadata and assets
└── docs/            # Project documentation
```

## Quick Start

### Backend Setup

1. Create a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the API server:
```bash
cd app
uvicorn main:app --reload
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the game:
```bash
cd game
python main.py
```

### Blockchain Setup

1. Install dependencies:
```bash
cd blockchain
npm install
```

2. Deploy contract:
```bash
npx hardhat run scripts/deploy.js --network <your-network>
```

### Environment Variables

Create a `.env` file in the root directory with:

```
# Backend
API_URL=http://localhost:8000

# Blockchain
INFURA_URL=your_infura_url
PRIVATE_KEY=your_private_key

# IPFS
PINATA_API_KEY=your_pinata_api_key
PINATA_SECRET_KEY=your_pinata_secret_key
```

## Features

- NFT-based inventory system
- Real-time game interaction
- Blockchain integration
- IPFS metadata storage
- Wallet connection

## Development Team

- Backend Developer: [Name]
- Frontend Developer: [Name]
- Blockchain Developer: [Name]

## License

MIT License 