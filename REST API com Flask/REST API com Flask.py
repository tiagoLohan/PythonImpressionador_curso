from flask import Flask
import pandas as pd

tabela = pd.read_excel("REST API com Flask/Vendas - Dez.xlsx")

app = Flask("__name__")


@app.route("/")
def faturamento():
  fat_valor = float(tabela["Valor Final"].sum())
  return {"Faturamento": fat_valor}


@app.route("/vendas/produtos")
def vendas_produtos():
  tabela_venda_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
  dic_vendas_produtos = tabela_venda_produtos.to_dict()
  return dic_vendas_produtos


@app.route("/vendas/produtos/<produto>")
def produto_especifico(produto):
  tabela_venda_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
  if produto in tabela_venda_produtos.index:
    vendas_produto = tabela_venda_produtos.loc[produto]
    dic_vendas_produto = vendas_produto.to_dict()
    return dic_vendas_produto
  else:
    return {produto: 'Inexistente'}

app.run()



