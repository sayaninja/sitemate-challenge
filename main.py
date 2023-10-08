from fastapi import FastAPI
from api.endpoints import issues
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(issues.router, prefix="/issues", tags=["issues"])
