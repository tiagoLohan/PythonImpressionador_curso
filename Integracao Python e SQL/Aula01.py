import pyodbc
import pandas as pd
import sqlite3
# print(pyodbc.drivers()) 

banco1 = "Integracao Python e SQL/salarios.sqlite"
banco2 = "Integracao Python e SQL/chinook.db"

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
           "Server=localhost;"
           f"Database={banco2}")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#  <------------ CREATE ----------->

# cursor.execute("""
# INSERT INTO albums (Title, ArtistId)
# VALUES
# ('Lira Rock', 4)
# """)

# cursor.commit()

# cursor.close()
# conexao.close()

#  <------------ CREATE ----------->

#  <------------ READ ----------->

# cursor.execute("""
# SELECT * FROM customers
# """)

# valores = cursor.fetchall()
# descricao = cursor.description
# colunas = [ coluna[0] for coluna in descricao]


# tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)

# print(tabela_clientes)


# cursor.close()
# conexao.close()


#  <------------ READ ----------->

#  <------------ READ COM PANDAS ----------->

# conexao = sqlite3.connect(banco2)

# tabela_cientes  = pd.read_sql("SELECT * FROM customers", conexao)

# print(tabela_cientes)

# conexao.close()

#  <------------ READ COM PANDAS ----------->

#  <------------ UPDATE ----------->

# cursor.execute("""
# UPDATE customers SET Email='lira@embraer.com.br' WHERE Email='luisg@embraer.com.br'
# """)


# cursor.commit()
# cursor.close()
# conexao.close()


#  <------------ UPDATE ----------->

#  <------------ DELETE ----------->

cursor.execute('''
DELETE FROM albums WHERE AlbumId=2
''')



cursor.commit()
cursor.close()
conexao.close()

#  <------------ DELETE ----------->


