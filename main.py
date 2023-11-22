import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.routes import discover, execute, abort, status

# add dot env
load_dotenv()

app = FastAPI()

origins = os.environ.get('ALLOW_ORIGINS')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(discover.router)
app.include_router(execute.router)
app.include_router(abort.router)
app.include_router(status.router)

# Config App
host = os.environ.get('APP_HOST', default='0.0.0.0')
port = os.environ.get('APP_PORT', default='8000')
isReload = os.environ.get('IS_RELOAD', default=False)
if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=int(port), reload=isReload)
