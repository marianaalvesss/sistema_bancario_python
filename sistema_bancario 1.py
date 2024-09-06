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

saldo = 0
saldo_atualizado = 0
opcao = -1

valor_depositado = 0
valor_indicado_saque = 0

depositos = []  # Lista para armazenar todos os depósitos
saques = [] # Lista para armazenar todos os saques

limite_saques = 3  # Limite máximo de saques permitidos
contagem_saques = 0  # Contador de saques realizados

while opcao != 0:
        opcao = int(input("[1] depositar \n[2] sacar \n [3] extrato \n [0] sair: "))
        if opcao == 1:
               deposito = float(input("Informe o valor a ser depositado:"))
               if deposito > 0:
                saldo_atualizado = deposito
                depositos.append(deposito)  # Armazena o depósito na lista
                valor_depositado = sum(depositos)  # Atualiza o valor total dos depósitos
                print(f"Valor de R$ {deposito:.2f} depositado com sucesso!")
               else:
                print("O valor depositado é inválido, tente novamente!")
        elif opcao == 2:
               # Verifica se já foram realizados 3 saques
               if contagem_saques >= limite_saques:
                   print("Limite de saques atingido! Não é possível realizar mais saques.")   
               else:
                   saque = float(input("Informe o valor desejado para saque: "))
                   valor_indicado_saque = saque
                   saldo_pos_saque = saldo_atualizado - saque
                   if saque > 0:
                       valor_a_sacar = saque
                       print("Aguarde, validando operação...")
                       if saldo_pos_saque > 0:
                           saques.append(saldo_pos_saque) #Armazena o saque na lista
                           valor_sacado = sum(saques) # Atualiza o valor total dos saques
                           contagem_saques += 1  # Incrementa o contador de saques
                           print(f"Saque de R$ {valor_indicado_saque:.2f} realizado com sucesso!")
                       else:
                           print("Saldo Inválido. Tente novamente!")
        elif opcao == 3:
                print("\n=== Extrato da Conta ===")
                #condicao caso nao tenha valor depositado e nao tenha saque
                if (valor_depositado < 0 or valor_depositado is None) and (valor_indicado_saque < 0 or valor_indicado_saque is None):
                    extrato = saldo_atualizado
                    print(f"Não foi realizada nenhuma transação de saque. \n Não foi realizado nenhum depósito. \n O saldo atual da conta é de R$ {extrato:.2f}")
                #teve valor depositado mas nenhum sacado
                if valor_depositado > 0 and (valor_indicado_saque < 0 or valor_indicado_saque is None):
                    extrato = saldo_atualizado
                    print(f"Não foi realizada nenhuma transação de saque. \n O último deposito realizado foi de R$ {valor_depositado:.2f}.\n O saldo atual da conta é de R$ {extrato:.2f}")
                #não teve valor depositado apenas saque
                if (valor_depositado < 0 or valor_depositado is None) and valor_indicado_saque > 0:
                   extrato = saldo - valor_indicado_saque
                   print(f"O ultimo saque realizado foi de R$ {valor_indicado_saque:.2f}. \n Não foi realizado nenhum depósito.\n O saldo atual da conta é de R$ {extrato:.2f}")
                #teve valor depositado e teve saque
                else:
                    extrato = saldo_atualizado - valor_indicado_saque
                    print(f"O último saque realizado foi de R$ {valor_indicado_saque:.2f}. \n O último deposito realizado foi de R$ {valor_depositado:.2f}.\n O saldo atual da conta é de R$ {extrato:.2f}")
        elif opcao == 0:
            break
        else:
            print("Operação Inválida, por favor, selecione novamente a opção desejada.")
                
               
            
