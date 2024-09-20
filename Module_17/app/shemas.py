from pydantic import BaseModel

class CreateProduct(BaseModel):
    name: str
    description: str
    price: float
    img_url: str
    stock: int
    category: int


class CreateCategory(BaseModel):
    name: str
    parent_id: int | None


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateUser(UpdateUser):
    username: str


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(CreateTask):
    pass

