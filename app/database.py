from pymongo import MongoClient 
from .config import MONGOURL, MONGODB, MONGOCOLLECTION 

client = MongoClient(MONGOURL)
db = client[MONGODB]
mensagens = db["mensagens"]
usuarios = db["mensagens"]

from datetime import datetime

async def salvar_mensagem(sala_id: str, nickname: str, mensagem: str):
    await mensagem.insert_one(
        {
            "sala_id": sala_id,
            "nickname": nickname,
            "menssagem": mensagem,
            "timestamp": datetime.utcnow()
        }
    )