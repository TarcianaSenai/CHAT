# app/routes/http.py


from fastapi import APIRouter
# from ..manager import ConnectionManager
# from ..database import get_history

router = APIRouter()

@router.get("/")
async def root():
        return{"massage": "Bem-Vindo! Conecte-se /we/{sala_id}?nickname=Seunome"}

@router.get ("/slas")
async def list_salas():
        return{"message": "Aqui teremos as salas"}


@router.get ("/slas")
async def history(sala_id: str):
        return{"message": "Aqui teremos o historico"}

