from fastapi import FastAPI
from .routes import router as ApplicantRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {
        "message": "¡Bienvenido a Tenpo Lab! La documentación está en la ruta /docs"
    }

app.include_router(ApplicantRouter, prefix="/trainee", tags=["Trainee"])