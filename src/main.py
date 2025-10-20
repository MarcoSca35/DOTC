"""Application main module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.db import Base, engine
from api import api_router
from ws_service import websocket_router

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

# Connecting to DB and creating tables
print("🟡 Creando tablas...")
Base.metadata.create_all(engine)
print("🟢 Tablas creadas con éxito")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API funcionando correctamente 🚀"}


# Including routers
app.include_router(api_router)
app.include_router(websocket_router)
