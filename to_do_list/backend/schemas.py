from pydantic import BaseModel
from typing import Optional
from datetime import datetime

PriorityOptions = ("low", "medium", "high")

class TaskCreate(BaseModel):
    # Campos que o usuário DEVE enviar:
    title: str

    # Campos que o usuário PODE enviar (opcionais):
    description: optional[str] = None
    priority: Optional[str] = "medium"  # Valores possíveis: "low", "medium", "high"

    # Campos que NÃO vêm do usuário:
    created_at: Optional[datetime] = None
    completed: Optional[bool] = False
    id: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None  # Valores possíveis: "low", "medium", "high"
    completed: Optional[bool] = false

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: str
    created_at: datetime
    completed: bool
