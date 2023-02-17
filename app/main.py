from app.config import settings
from app.api import api
from fastapi import FastAPI
import uvicorn


app = FastAPI()
app.include_router(api.router)


if __name__ == '__main__':
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
