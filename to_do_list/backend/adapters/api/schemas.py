from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: str
    title: str
    completed: bool
    created_at: str