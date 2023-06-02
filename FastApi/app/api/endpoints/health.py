from datetime import datetime

from fastapi import APIRouter

import  google.cloud.logging as gcloudlog
import logging

from core import config
from models.health import HealthcheckResponse

cliente_logging= gcloudlog.Client()
cliente_logging.setup_logging()

router = APIRouter()

@router.get("", response_model=HealthcheckResponse, tags=["health"])
def healthcheck() -> HealthcheckResponse:
    message = "HEALTH [healthcheck] >>  We're on the air."
    logging.info(message)
    return HealthcheckResponse(
        message=message, version=config.VERSION, time=datetime.now()
    )