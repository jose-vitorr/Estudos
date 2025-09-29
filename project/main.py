from fastapi import FastAPI

app = FastAPI()

# Rota raiz
@app.get("/")
def read_root():
    return "Hello World"

# Lista de nomes
nomes = ["Alice", "Bob", "Charlie"]

# Lista todos os nomes
@app.get("/{nomes}") 
def read():
    return {"nomes": nomes}

# Retorna o nome pelo índice
@app.get("/nome/{index}")
def nome_por_indice(index: int):
    return {"nome": nomes[index]}