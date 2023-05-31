from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hola mundo!"

@app.get("/ferran")
async def saludo_ferran ():
    return {"message": "Hola Ferran"}