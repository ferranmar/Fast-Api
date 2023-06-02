import time
from typing import Any, Callable
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from core import config
from api import urls

app = FastAPI(title=config.TITLE, version=config.VERSION)

# ORIGINS
if config.ORIGINS:
    ORIGINS = config.ORIGINS.split(",")
    print("Origins: {}".format(ORIGINS))
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# MIDDLEWARE   
@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable) -> Any:
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# ROUTERS
app.include_router(urls.router,  prefix=config.API_VERSION)
