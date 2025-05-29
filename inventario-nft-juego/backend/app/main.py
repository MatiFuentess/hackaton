from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crear la aplicación FastAPI
app = FastAPI(
    title="Inventory NFT Game API",
    description="API para el juego de inventario NFT",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API de Inventario NFT Game funcionando"}

@app.get("/test")
async def test():
    return {"status": "ok", "message": "Endpoint de prueba funcionando"} 