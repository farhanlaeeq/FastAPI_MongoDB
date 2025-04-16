from fastapi import FastAPI
from api.api import api_router

app = FastAPI(title="ERP Backend")
app.include_router(api_router, prefix="/api")