from fastapi import FastAPI
from routers import products, saludo

app = FastAPI()

app.include_router(products.router)
app.include_router(saludo.router)

@app.get("/")
async def inicio():
    return "Hola FastApi"