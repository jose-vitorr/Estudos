from typing import List, Optional
import uuid

from domain.entities import Todo
from domain.repositories import TodoRepository

class TodoUseCases:
    def __init__(self, repository: TodoRepository):
        self.repository = repository
    
    def create_todo(self, title: str) -> Todo:
        if not title or len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        
        todo = Todo(
            id=str(uuid.uuid4()),
            title=title.strip()
        )
        return self.repository.create(todo)
    
    def list_todos(self) -> List[Todo]:
        return self.repository.get_all()
    
    def toggle_todo(self, todo_id: str) -> Optional[Todo]:
        todo = self.repository.get_by_id(todo_id)
        if not todo:
            return None
        
        if todo.completed:
            todo.mark_incomplete()
        else:
            todo.mark_completed()
        
        return self.repository.update(todo)
    
    def delete_todo(self, todo_id: str) -> bool:
        return self.repository.delete(todo_id)