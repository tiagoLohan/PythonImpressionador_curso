
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


estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50

print("Produtos que precisam reabastecer:")
print()
for i, produto in enumerate(estoque):
    if produto < nivel_minimo:
        print(f"'{produtos[i]}' possui apenas '{produto}' unidades em estoque! REABASTECER")
        

