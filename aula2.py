# from fastapi import FastAPI

# app = FastAPI()

# dados = {
#     1: {"nome": "Tiago Lohan", "idade": 30, "salario": 8000},
#     2: {"nome": "Matheus", "idade": 27, "salario": 5000},
#     3: {"nome": "Lico", "idade": 33, "salario": 4000}
# }


# @app.get("/")
# def home():
#     return dados

# @app.get("/quantidade")
# def quantidade_users():
#     return {"Quantidade de usuários": len(dados)}

# @app.get("/usuario/{id}")
# def busca_usuario(id: int):
#     if id in dados:
#         return dados[id]
#     else:
#         return {"ERROR": "ID não localizado."}

# /////////////////////////////////////////////////////////////////////////////////////////

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_languages():
    return { "success" : "foi" }