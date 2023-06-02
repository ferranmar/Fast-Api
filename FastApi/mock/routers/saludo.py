from fastapi import APIRouter

router = APIRouter(prefix="/saludo")

@router.get("/")
async def saludo_ferran():
    return "Hola Ferran"