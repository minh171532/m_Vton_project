import os

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from config import APP_PATH, LOGGER, CONFIG
# from app.routers import setting, authen, user, item
# from app.routers import authen, user, item
from app.routers import user, item
from app.logs.middleware import LogMiddleware
from app.utils.app_exceptions import app_exception_handler, AppExceptionCase
from app.utils.request_exceptions import http_exception_handler, request_validation_exception_handler


app = FastAPI()
LOGGER.info("\n\n\nStart Prototype UI webapp! \n")
# LOGGER.info("{}".format(show_config()))

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Set statics
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/assets", StaticFiles(directory="app/static/reactjs/assets/"), name="assets")
app.mount("/images", StaticFiles(directory=CONFIG.ITEM_DIR), name="images")


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)

# The default route, which shows the default web page


@app.get("/")
async def read_index():
    return FileResponse(os.path.join(APP_PATH, "static", "reactjs", "index.html"))

# Add middleware
app.add_middleware(LogMiddleware)

# Include routers
# app.include_router(setting.router)
# app.include_router(authen.router)
app.include_router(user.router)
app.include_router(item.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=5111, reload=True)
