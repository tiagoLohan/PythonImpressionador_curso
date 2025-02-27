import pyodbc
print(pyodbc.drivers())

banco1 = "Integracao Python e SQL/salarios.sqlite"
banco2 = "Integracao Python e SQL/chinook.db"

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
           "Server=localhost;"
           f"Database={banco2}")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#  <------------ CREATE ----------->

cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES
('Lira Rock', 4)
""")

cursor.commit()





cursor.close()
conexao.close()