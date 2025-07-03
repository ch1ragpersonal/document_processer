from fastapi import APIRouter

router = APIRouter()

@router.get("/documents")
async def get_documents():
    return {"message": "Hello World"}