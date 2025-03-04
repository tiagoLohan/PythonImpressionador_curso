import mysql.connector

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lohanDev",
  database="bdaulapython",
)

cursor = conexao.cursor()

# CRUD

####################  CREATOR  ####################
# nome_produto = "chocolate"
# valor = 15

# comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
# cursor.execute(comando, (nome_produto, valor))
# conexao.commit()

# cursor.close()
# conexao.close()

####################  READE  ####################

# comando = 'SELECT * FROM vendas'
# cursor.execute(comando)
# valores = cursor.fetchall()
# print(valores)


# cursor.close()
# conexao.close()


####################  UPDATE  ####################

  # nome_produto = "todynho"
  # novo_valor = 6
  # comando = 'UPDATE vendas SET valor = %s WHERE nome_produto = %s'
  # cursor.execute(comando, (novo_valor, nome_produto))
  # conexao.commit()



  # cursor.close()
  # conexao.close()

####################  DELETE  ####################

nome_produto = "todynho"

comando = 'DELETE FROM vendas WHERE nome_produto = %s'
cursor.execute(comando, (nome_produto,))
conexao.commit()



cursor.close()
conexao.close()
