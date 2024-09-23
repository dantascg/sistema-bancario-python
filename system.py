import textwrap

def menu():
    menu ="""
    ######### BANCO DOS MITOS ##########

    [d]\t - DEPÓSITO
    [s]\t - SAQUE
    [v]\t - VISUALIZAR EXTRATO
    [n]\t - NOVO CLIENTE
    [c]\t - NOVA CONTA
    [p]\t - LISTAR CONTAS
    [q]\t - SAIR


    ####################################\n"""
    return input(textwrap.dedent(menu))

def realizar_deposito(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"\n\t● Depósito: R${valor:.2f}"
            print("☯︎☯︎ Valor depositado! ☯︎☯︎")
        else:
            print("✖✖ Operação não realizada pois o valor inserido é inválido! ✖✖")
        return saldo, extrato
    
def realizar_saque(saldo, valor, extrato, numerosaques, LIMITE_SAQUES, limite):
    excedeu_limite = valor > limite
    valor_invalido = valor <= 0
    excedeu_saldo = valor > saldo

    if valor_invalido:
            print("✖✖ Operação não realizada pois o valor inserido é inválido! ✖✖")
    elif excedeu_limite:
            print("✖✖ Operação não realizada pois o valor ultrapassa o limite de R$500,00! ✖✖")
    elif excedeu_saldo:
            print("✖✖ Operação não realizada pois você não possui saldo o suficiente! ✖✖")
    elif numerosaques < LIMITE_SAQUES:
            saldo -= valor
            print("☯︎☯︎ Saque realizado! ☯︎☯︎")
            extrato += f"\n\t● Saque: R${valor:.2f}"
            numerosaques += 1
    else:
            print("✖✖ Operação não realizada pois o limite de saques foi excedido! ✖✖")
    return saldo, extrato, numerosaques


def visualizar_extrato(saldo, valor, extrato, numerosaques):
    print(f"""
\t============================
\t          EXTRATO
\t============================
\t>> Seu saldo: R${saldo:.2f} <<""")
    print(extrato)
    print(f"\n\tNúmero de saques: {numerosaques}")
    print("\t============================")
    return extrato, numerosaques

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (SOMENTE NÚMEROS): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("✖✖ Já existe usuário com esse CPF! ✖✖")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade - estado): ")

    usuarios_dict = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuarios_dict.copy())

    print("☯︎☯︎ Usuário criado com sucesso! ☯︎☯︎")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (SOMENTE NÚMEROS): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("☯︎☯︎ Conta criada! ☯︎☯︎")
    else:
         print("✖✖ Usuário não encontrado, criação de conta encerrada! ✖✖")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        Cliente:\t{conta['numero_conta']}        
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
    
def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    extrato = " "
    saldo = 0
    limite = 500
    numerosaques = 0
    valor = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input(("Informe o valor do depósito: ")))
            saldo, extrato = realizar_deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input(("Informe o valor do saque: ")))
            saldo, extrato, numerosaques = realizar_saque(saldo, valor, extrato, numerosaques, LIMITE_SAQUES, limite)
            
        elif opcao == 'v':
            visualizar_extrato(saldo, valor, extrato, numerosaques)
        elif opcao == 'n':
            criar_usuario(usuarios)
        elif opcao == 'c':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)
        elif opcao == 'p':
            listar_contas(contas)
        elif opcao == 'q':
            break
        else:
            print("✖✖ Operação não realizada pois o valor informado para seleção é inválido! ✖✖")
main()