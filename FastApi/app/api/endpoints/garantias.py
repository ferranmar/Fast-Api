import  google.cloud.logging as gcloudlog
import logging 

from datetime import date, datetime
from models.health import HealthcheckResponse
from services.garantias import garantias as services
from fastapi.routing import APIRouter
from starlette import status
from starlette.responses import Response
from starlette.requests import Request

from core import config


router = APIRouter()

cliente_logging= gcloudlog.Client()
cliente_logging.setup_logging()

@router.get('/importData')
def garantias(request: Request):
    """
    """    
    logging.info("garantias [ENDPOINTS/importData] >> Receiving locations... ")
    
    it_worked = services.start("/importData")

    return Response(status_code=status.HTTP_200_OK)
