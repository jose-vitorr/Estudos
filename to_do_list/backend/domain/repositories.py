from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities import Todo

class TodoRepository(ABC):
    """Port - Interface que define o contrato"""
    
    @abstractmethod
    def create(self, todo: Todo) -> Todo:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Todo]:
        pass
    
    @abstractmethod
    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        pass
    
    @abstractmethod
    def update(self, todo: Todo) -> Optional[Todo]:
        pass
    
    @abstractmethod
    def delete(self, todo_id: str) -> bool:
        pass