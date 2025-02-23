import json
import time
import os


def adicionar_item(compras, item, qtd):
    compras[item] = qtd

def remover_item(compras, item):
    if item in compras:
       del compras[item]

def visualizar_compras(compras):
    for item, qtd in compras.items():
       print(f"{item}: {qtd}")
    print()
    print("Pressione enter para continuar")
    input()

def salvar_compras(compras, nome_arquivo):
    with open(f"Lista de Compras/{nome_arquivo}", "w") as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(f"Lista de Compras/{nome_arquivo}", "r") as arquivo:
        return json.load(arquivo)
      
def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Adicionar ítem")
        print("2 Remover ítem")
        print("3 Visualizar lista")
        print("4 Salvar e sair")
        print("5 Sair sem salvar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o nome do ítem: ")
            qtd = int(input("Digite a quantidade: "))
            adicionar_item(compras, item, qtd)

        elif escolha == "2":
            item = input("Digite o nome do ítem que deseja remover: ")
            if item in compras:
                remover_item(compras, item)
            else:
                print("Ítem não localizado na lista")

        elif escolha == "3":
            visualizar_compras(compras)
        
        elif escolha == "4":
            if nome_arquivo is None:
                nome_arquivo = input("Digite o nome do arquivo para salvar: ")
                salvar_compras(compras, nome_arquivo)
            
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"

            salvar_compras(compras, nome_arquivo)
            break

        elif escolha == "5":
            break
        else:
            print("Opção inválida")
            time.sleep(1)
        

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Criar uma nova lista de compras")
        print("2 Carregar uma lista existente")
        print("3 Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)

        elif escolha == "2":
            print("Listas disponíveis:")
            arquivos = [arquivo for arquivo in os.listdir("Lista de Compras") if arquivo.endswith(".json")]

            if not arquivos:
                print("Nenhuma lista encotrada")
                time.sleep(2)
                continue

            for i, arquivo in enumerate(arquivos, 1):
                print(f"{i} {arquivo}")
            
            escolha = int(input("Escolha uma lista para carregar (0 se nenhuma): "))

            if escolha == 0:
                continue
            
            elif escolha < 0 or escolha > len(arquivos):
                print("Opção inválida")
                time.sleep(1)
                continue
            
            compras = carregar_compras(arquivos[escolha - 1])  
            gerenciar_compras(compras, arquivos[escolha - 1])
            
        
        elif escolha == "3":
            break
        
        else:
            print("Opção inválida")
            time.sleep(1)



if __name__ == "__main__":
    main()
