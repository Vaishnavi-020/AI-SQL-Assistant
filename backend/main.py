from fastapi import FastAPI
from .router.query_router import router as QueryRouter

app=FastAPI()

app.include_router(QueryRouter)
