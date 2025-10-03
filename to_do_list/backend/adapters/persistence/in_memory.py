from typing import List, Optional

from domain.entities import Todo
from domain.repositories import TodoRepository


class InMemoryTodoRepository(TodoRepository):
    """Adapter - Implementação em memória"""
    
    def __init__(self):
        self.todos: dict[str, Todo] = {}
    
    def create(self, todo: Todo) -> Todo:
        self.todos[todo.id] = todo
        return todo
    
    def get_all(self) -> List[Todo]:
        return list(self.todos.values())
    
    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        return self.todos.get(todo_id)
    
    def update(self, todo: Todo) -> Optional[Todo]:
        if todo.id in self.todos:
            self.todos[todo.id] = todo
            return todo
        return None
    
    def delete(self, todo_id: str) -> bool:
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False
