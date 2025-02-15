
# nome = "TiagoLohan@gmail.com"


# print(nome[-1])
# print(len(nome))
# print(nome[:10])
# print(nome[11:])


###########################################################

# Aula 7 de 14: Print e Join em Listas

# lista = ["Celular", "Caneta", "Bola", "Bicicleta", "Copo", "Tv", "Diploma"]


# print(lista)
# print()
# print("\n".join(lista))


# texto = "celular, caneta, bola, bicicleta, copo, tv, diploma"
# nova_lista = texto.split(", ")
# print()
# print(nova_lista)


###########################################################

# Aula 3 de 12: For e If

# vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
# meta = 1000

# # metas_batidas = 0

# # for venda in vendas:
# #     if venda >= meta:
# #         metas_batidas += 1

# # qtd_vendedores = len(vendas)
# # percentual_meta_batida = metas_batidas / qtd_vendedores

# # print(f"{percentual_meta_batida:.0%} de meta batida")


# for i, venda in enumerate(vendas):
#     print(f"{i+1} - {venda}")


###########################################################

# Aula 4 de 12: Enumerate - For com item e índice


# estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
# produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
# nivel_minimo = 50

# print("Produtos que precisam reabastecer:")
# print()
# for i, produto in enumerate(estoque):
#     if produto < nivel_minimo:
#         print(f"'{produtos[i]}' possui apenas '{produto}' unidades em estoque! REABASTECER")
        


###########################################################

# cont = 0
# while cont != 0:
#   print(f"{cont+1} - Tiago e Matheus ❤")
#   cont += 1


###########################################################


# def area_a_ser_pintada():
#     area = int(input("Digite o total da área em m²: "))
#     return area

# def calcular_litros_de_tinta(area):
#     litros = area / 6
#     return litros

# def calcular_latas_de_tinta(litros):
#     latas = litros / 18
#     if int(latas) < latas:
#         latas = int(latas) + 1
#     return latas

# def calcular_preco(latas, lata_valor_unit):
#     preco = float(latas * lata_valor_unit)
#     return preco


# area = area_a_ser_pintada()
# litros = calcular_litros_de_tinta(area)
# latas = calcular_latas_de_tinta(litros)
# preco = calcular_preco(latas, 80)

# print(f"Qts de latas: {latas}")
# print(f"Preço total: {preco}")

###########################################################

# import webbrowser

# webbrowser.open_new("http://totvs.com.br")


###########################################################

# import time

# tempo_inicial = time.time()

# for i in range(100000000):
#   pass

# tempo_final = time.time()

# tempo_total = tempo_final - tempo_inicial

# print(tempo_total)

# hoje = time.localtime()
# print(hoje)

# dia = hoje.tm_mday
# mes = hoje.tm_mon
# ano = hoje.tm_year

# print(f"Hoje é {dia}/{mes}/{ano}")


# hoje = time.localtime()

# print(hoje)
# print(time.strftime("%d/%m/%Y as %H:%M:%S", hoje))

###########################################################

# from datetime import datetime

# agora = datetime.now()

# print(agora)
# print(f"Data: {agora.date()}")
# print(f"Hora: {agora.time()}")
# print()

# print(f"Dia: {agora.day}")
# print(f"Mês: {agora.month}")
# print(f"Ano: {agora.year}")

# from datetime import datetime, timedelta

# data_atual = datetime.now()
# print(data_atual)

# data_futura = data_atual + timedelta(days=11)
# print(data_futura)

# data_passada = data_atual - timedelta(days=40)
# print(data_passada)

# bday = datetime(1990, 9, 10, 18, 00, 00)
# print(bday)

# data_atual = datetime.now()
# ano_novo = datetime(1990, 2, 10)

# resto = data_atual - ano_novo

# print(int(resto.days / 365))

# hoje = datetime.now()
# data_nascimento = datetime(1990, 9, 10, 18, 00)

# idade = hoje - data_nascimento

# print(int(idade.days / 365))
# print(hoje == data_nascimento)

###########################################################

# vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 1433, 2100, 2762]
# meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

# import matplotlib.pyplot as plt

# plt.plot(meses, vendas_meses)
# plt.ylabel("Vendas")
# plt.xlabel("Meses")
# plt.axis([0, 12, 0, max(vendas_meses) + 500])
# plt.show()


# def maiuscula(texto):
#   return texto.upper()


# lista = list(map(maiuscula, meses))
# lista2 = [mes.upper() for mes in meses]

# texto = "tiago lohan"

# nome = lambda x: x.upper()

# print(nome(texto))

# imposto = 0.3

# novo_valor = lambda x, y: x + (x * y)

# print(novo_valor(100, imposto))

# vendas_novo = list(map(lambda x: x + 1, vendas_meses))

# print(vendas_novo)

###########################################################

# import pandas as pd

# df = pd.DataFrame(
#     {
#         "Name": [
#             "Tiago Lohan",
#             "Diego Lohan"
#         ],
#         "Age": [
#             34,
#             27
#         ],
#         "Marital Status": [
#             "Married",
#             "Married"
#         ]
#     }
# )

# print(df["Name"])


###########################################################

with open(r"C:\Users\tiiag\Downloads\Alunos.txt", "r") as arquivo:
 linhas = arquivo.readlines()
 del linhas[:4]



for linha in linhas:
 email, origem = linha.split(",")
