import os
import secrets
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, status
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.exceptions import HTTPException

from src.shared import api_health_check
from src.shared.utils.logger import logger
from src.wsaa.api import wsaa_endpoints
from src.wsaa.api.afip_token_scheduler import start_scheduler, stop_scheduler
from src.wsfev1.api import wsfev1_endpoints
from src.wsfev1.health_checks import wsfev1_health_checks

load_dotenv(override=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
    stop_scheduler()

app = FastAPI(lifespan=lifespan)
app.include_router(api_health_check.router)
app.include_router(wsaa_endpoints.router)
app.include_router(wsfev1_endpoints.router)
app.include_router(wsfev1_health_checks.router)

# ===================
# === DOCS CONFIG ===
# ===================

security = HTTPBasic()

USERNAME = os.getenv('DOCS_USERNAME')
PASSWORD = os.getenv('DOCS_PASSWORD')

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate" : "Basic"}
        )
    return True

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui(credentials: bool = Depends(verify_credentials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Docs")

@app.get("/openapi.json", include_in_schema=False)
def openapi(credentials: bool = Depends(verify_credentials)):
    return JSONResponse(
        get_openapi(title="My API", version="1.0.0", routes=app.routes)
    )