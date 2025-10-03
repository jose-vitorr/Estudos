from fastapi import APIRouter, HTTPException
from typing import List

from adapters.api.schemas import TodoCreate, TodoResponse
from use_cases.todo_use_cases import TodoUseCases
from domain.repositories import TodoRepository

def create_router(use_cases: TodoUseCases) -> APIRouter:
    """Factory function to create router with injected dependencies"""
    router = APIRouter(prefix="/todos", tags=["todos"])
    
    @router.post("", response_model=TodoResponse, status_code=201)
    def create_todo(data: TodoCreate):
        """Create a new todo item"""
        try:
            todo = use_cases.create_todo(data.title)
            return TodoResponse(
                id=todo.id,
                title=todo.title,
                completed=todo.completed,
                created_at=todo.created_at.isoformat()
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @router.get("", response_model=List[TodoResponse])
    def list_todos():
        """List all todo items"""
        todos = use_cases.list_todos()
        return [
            TodoResponse(
                id=t.id,
                title=t.title,
                completed=t.completed,
                created_at=t.created_at.isoformat()
            )
            for t in todos
        ]
    
    @router.patch("/{todo_id}/toggle", response_model=TodoResponse)
    def toggle_todo(todo_id: str):
        """Toggle todo completion status"""
        todo = use_cases.toggle_todo(todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return TodoResponse(
            id=todo.id,
            title=todo.title,
            completed=todo.completed,
            created_at=todo.created_at.isoformat()
        )
    
    @router.delete("/{todo_id}", status_code=204)
    def delete_todo(todo_id: str):
        """Delete a todo item"""
        success = use_cases.delete_todo(todo_id)
        if not success:
            raise HTTPException(status_code=404, detail="Todo not found")
        return None
    
    return router