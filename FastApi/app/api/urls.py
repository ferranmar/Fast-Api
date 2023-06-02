from email.quoprimime import header_check
from fastapi.routing import APIRouter
from api.endpoints import health, contratacion, garantias

router = APIRouter()
router.include_router(health.router, prefix='/health', tags=['health'])
router.include_router(contratacion.router, prefix='/contratacion', tags=['contratacion'])
router.include_router(garantias.router, prefix='/garantias', tags=['garantias'])