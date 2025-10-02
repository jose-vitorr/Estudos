from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="To-Do API (Arquitetura Hexagonal)")

# CORS para o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency Injection
repository = InMemoryTodoRepository()
use_cases = TodoUseCases(repository)

@app.post("/todos", response_model=TodoResponse)
def create_todo(data: TodoCreate):
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

@app.get("/todos", response_model=List[TodoResponse])
def list_todos():
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

@app.patch("/todos/{todo_id}/toggle")
def toggle_todo(todo_id: str):
    todo = use_cases.toggle_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        completed=todo.completed,
        created_at=todo.created_at.isoformat()
    )

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    success = use_cases.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)