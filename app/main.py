# from fastapi import FastAPI
# from app.routers.string_utils import router as string_utils_router

# app = FastAPI()

# app.include_router(string_utils_router)

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI String Utils API!"}


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/")
async def count_characters(input: TextInput):
    return {"character_count": len(input.text)}