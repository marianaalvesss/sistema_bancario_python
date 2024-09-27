#Operação de depósito 
#Deve ser possível depositar valores 
# positivos para a minha conta bancária. 
# A v1 do projeto trabalha apenas com 1 usuário, 
# dessa forma não precisamos nos preocupar em 
# # identificar qual é o número da agencia e 
# conta bancária. 

#Operação de saque 
#O sistema deve permitir realizar 3 saques diários com limite 
# máximo de 500 por saque. Caso o usuário não tenha saldo em conta, 
# o sistema deve exibir uma mensagem informando que não será possível
# sacar o dinheiro por falta de saldo. 

#Operação de extrato 
# deve ser exibido o saldo atual da conta. 
# Os valores devem ser exibidos utilizando o formato R$xxx.xx 


#Versão 2
# Estabelecer um limite de 10 transacoes diárias para uma conta 
# Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia. 
# Mostre no extrato a data e hora das transações. 

#Versão 3
# Criar duas novas funções: cadastrar usuário e cadastrar conta bancária
#separar sacar depositar e visualizar historico em funções
# a função de saque deve receber os argumentos apenas por nome argumentos: saldo, valor, extrato, limite, numero_saques e limite_saques. SUgestão de retorno: saldo e extrato
# a função deposito deve receber os argumentos apenas por posição. Argumentos: saldo, valor e extrato. Sugestão de retorno: saldo e extrato
# a função extrato deve receber os argumentos por posicao e nome. Argumentos posicionais: saldo. Argumentos nomeados: extrato.
# o programa deve armazenar os usuários em uma lista, um usuário é composto por nome, data de nascimento, cpf e endereço. O endereço é uma string com formato logradouro, nro, bairro, cidade e estado.
# Deve ser armazenado somente os numeros do CPF. Não deve ser possível cadastrar dois usuários com o mesmo CPF.
# para criar a conta corrente o programa deve armazenar contas em uma lista, uma conta é composta por agencia, numero da conta e usuário. o numero da conta é sequencial iniciando em 1.
# O numero da agencia é fixo "0001". O usuário pode ter mais de uma conta mas uma conta pertence a apenas um usuário. Para vincular um usuário a uma conta filtre a lista de usuários
# buscando um nro de CPF informado para cada usuário da lista

from datetime import datetime

# Listas para armazenar os usuários e as contas
usuarios = []
contas = []
numero_conta_sequencial = 1  # Inicia o número da conta como 1
AGENCIA = "0001"  # Número fixo da agência

# Função para cadastrar usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado!")
            return

    # Cria o usuário
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    # Adiciona o usuário à lista
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

# Função para cadastrar conta bancária
def cadastrar_conta(cpf):
    global numero_conta_sequencial

    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Busca o usuário pelo CPF
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        # Cria a conta bancária
        conta = {
            'agencia': AGENCIA,
            'numero_conta': numero_conta_sequencial,
            'usuario': usuario_encontrado,
            'saldo': 0,  # Saldo inicial da conta
            'transacoes': []  # Histórico de transações (depósitos e saques)
        }

        # Adiciona a conta à lista de contas
        contas.append(conta)
        print(f"Conta número {numero_conta_sequencial} cadastrada para o usuário {usuario_encontrado['nome']}!")

        # Incrementa o número da conta para a próxima conta
        numero_conta_sequencial += 1
    else:
        print("Usuário não encontrado. Por favor, verifique o CPF.")

# Função para sacar
def sacar(*, conta, valor, limite_saques, numero_saques):
    if numero_saques >= limite_saques:
        print("Limite de saques atingido! Não é possível realizar mais saques.")
    elif valor > 0 and conta['saldo'] >= valor:
        conta['saldo'] -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta['transacoes'].append((f"Saque: R$ {valor:.2f}", data_hora))
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    elif valor <= 0:
        print("Valor de saque inválido.")
    else:
        print("Saldo insuficiente.")
    return conta['saldo'], conta['transacoes'], numero_saques

# Função para depositar
def depositar(conta, valor):
    if valor > 0:
        conta['saldo'] += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta['transacoes'].append((f"Depósito: R$ {valor:.2f}", data_hora))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")
    return conta['saldo'], conta['transacoes']

# Função para exibir o extrato
def extrato(conta):
    print("\n=== Extrato da Conta ===")
    if not conta['transacoes']:
        print("Não foram realizadas transações.")
    else:
        for transacao, data_hora in conta['transacoes']:
            print(f"{transacao} em {data_hora}")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

# Função para listar os usuários cadastrados
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")

# Função para listar as contas cadastradas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")

# Função para buscar conta pelo CPF
def buscar_conta_por_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            return conta
    return None

# Exemplo de uso:
limite_saques = 3  # Limite de saques por conta
numero_saques = 0  # Contagem de saques
contagem_transacoes = 0  # Contador de transações

while True:
    print("\n[1] Cadastrar Usuário\n[2] Cadastrar Conta\n[3] Depositar\n[4] Sacar\n[5] Extrato\n[6] Listar Usuários\n[7] Listar Contas\n[0] Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, nro, bairro, cidade - estado): ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == 2:
        cpf = input("Informe o CPF do usuário para vincular à conta: ")
        cadastrar_conta(cpf)

    elif opcao == 3:
        cpf = input("Informe o CPF para depósito: ")
        conta = buscar_conta_por_cpf(cpf)
        if conta:
            valor_deposito = float(input("Informe o valor a ser depositado: "))
            depositar(conta, valor_deposito)
        else:
            print("Conta não encontrada.")

    elif opcao == 4:
        cpf = input("Informe o CPF para saque: ")
        conta = buscar_conta_por_cpf(cpf)
        if conta:
            valor_saque = float(input("Informe o valor a ser sacado: "))
            conta['saldo'], conta['transacoes'], numero_saques = sacar(
                conta=conta,
                valor=valor_saque,
                limite_saques=limite_saques,
                numero_saques=numero_saques
            )
        else:
            print("Conta não encontrada.")

    elif opcao == 5:
        cpf = input("Informe o CPF para visualizar o extrato: ")
        conta = buscar_conta_por_cpf(cpf)
        if conta:
            extrato(conta)
        else:
            print("Conta não encontrada.")

    elif opcao == 6:
        listar_usuarios()

    elif opcao == 7:
        listar_contas()

    elif opcao == 0:
        break

    else:
        print("Opção inválida.")
