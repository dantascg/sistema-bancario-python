menu ="""
######### BANCO DOS MITOS ##########

    [d] - DEPÓSITO
    [s] - SAQUE
    [v] - VISUALIZAR EXTRATO
    [q] - SAIR

####################################\n"""

extrato = " "
saldo = 0
limite = 500
numerosaques = 0
LIMITE_SAQUES = 3
valor = 0


while True:
    opcao = str(input(menu))

    if opcao == 'd':
        valor = float(input(("Informe o valor do depósito: ")))
        if valor > 0:
            saldo += valor
            extrato += f"\n● Depósito: R${valor:.2f}"
            print("Valor depositado!!")
        else:
            print("Operação não realizada pois o valor informado é inválido")

    elif opcao == 's':
        valor = float(input(("Informe o valor do saque: ")))
        
        excedeu_limite = valor > limite
        valor_invalido = valor <= 0
        excedeu_saldo = valor > saldo

        if valor_invalido:
            print("Operação não realizada pois o valor inserido é inválido")
        elif excedeu_limite:
            print("Operação não realizada pois o valor ultrapassa o limite de R$500,00")
        elif excedeu_saldo:
            print("Operação não realizada pois você não possui saldo o suficiente")
        elif numerosaques < LIMITE_SAQUES:
            saldo -= valor
            print("Saque realizado!")
            extrato += f"\n● Saque: R${valor:.2f}"
            numerosaques += 1
        else:
            print("Operação não realizada pois o limite de saques foi excedido")
        
    elif opcao == 'v':
        print(f"""
    ============================
              EXTRATO
    ============================
    >> Seu saldo: R${saldo:.2f} <<""")
        print(extrato)
        print(f"\nNúmero de saques: {numerosaques}")
        print("============================")
    elif opcao == 'q':
        break
    
    else:
        print("Operação não realizada pois o valor informado para seleção é inválido")
