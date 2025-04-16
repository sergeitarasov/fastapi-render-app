from fastapi import FastAPI
from app.routers.string_utils import router as string_utils_router

app = FastAPI()

app.include_router(string_utils_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI String Utils API!"}