from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Todo:
    id: str
    title: str
    completed: bool = False
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def mark_completed(self):
        self.completed = True
    
    def mark_incomplete(self):
        self.completed = False