from ContasBanco import ContaCorrente, CartaoCredito

#programa
conta_lira = ContaCorrente("Lira", "111.222.333-45", 2545, 789685)

cartao_Lira = CartaoCredito("Lira", conta_lira) 


cartao_Lira.senha = "2345"
print(cartao_Lira.senha)


