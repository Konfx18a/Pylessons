from fastapi import APIRouter

router = APIRouter(prefix="/category", tags=['category'])

@router.get("/all_categories")
async def all_categories():
    pass

@router.post("/create")
async def create_categories():
    pass

@router.put("/update_categories")
async def update_categories():
    pass

@router.delete("/delete")
async def delete_categories():
    pass