from fastapi import FastAPI
from api.endpoints import issues_router
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(issues_router.router, prefix="/issues", tags=["issues"])
