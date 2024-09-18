from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=['user'])

@user_router.get("/all_users")
async def all_users():
    pass

@user_router.get("/user_id")
async def user_by_id():
    pass

@user_router.post("/create")
async def create_user():
    pass

@user_router.put("/update")
async def update_user():
    pass

@user_router.delete("/delete")
async def delete_user():
    pass