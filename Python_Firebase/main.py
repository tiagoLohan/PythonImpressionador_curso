import requests
import json
import pprint

link = "https://primeiroprojetolohan-default-rtdb.firebaseio.com/"


# Criar uma venda (POST)

# dados = {"cliente": "hanni", "preco": 100, "produto": "game"}
# r = requests.post(f"{link}/Vendas/.json", data=json.dumps(dados))
# print(r)
# print(r.text)

# dados2 = {"cliente": "caio", "preco": 300, "produto": "capacete"}
# r = requests.post(f"{link}/Vendas/.json", data=json.dumps(dados2))
# print(r)
# print(r.text)


# Listar todas as venda (GET)

# r = requests.get(f"{link}/Vendas/.json")
# retorno = r.json()
# retorno = dict(retorno)
# print(retorno)

# Buscar um id de vendas pelo nome do cliente (GET)

r = requests.get(f"{link}/Vendas/.json")
retorno = r.json()
print(r)
id_caio = None
for id, dados in retorno.items():
  cliente = dados["cliente"]
  if cliente == "caio":
    id_caio = id
print(id_caio)

# Editar uma venda pelo ID da venda (PATCH)

dados = {"preco": 180}
r = requests.patch(f"{link}/Vendas/{id_caio}/.json", data=json.dumps(dados))
print(r)
retorno = r.json()
print(retorno)


# Deletar uma venda pelo ID da venda (DELETE)

r = requests.delete(f"{link}/Vendas/{id_caio}/.json")
print(r)
retorno = r.json()
print(retorno)