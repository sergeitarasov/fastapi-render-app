from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/count-characters")
async def count_characters(input_string: str):
    if not isinstance(input_string, str):
        raise HTTPException(status_code=400, detail="Input must be a string")
    return {"character_count": len(input_string)}