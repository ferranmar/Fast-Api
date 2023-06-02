from fastapi import APIRouter

router = APIRouter(prefix="/products")

@router.get("/")
async def products():
    return ["Producto1","Producto2","Producto3"]