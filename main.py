from fastapi import FastAPI
from api.endpoints import issues

app = FastAPI()

app.include_router(issues.router, prefix="/issues", tags=["issues"])
