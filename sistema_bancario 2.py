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

from datetime import datetime

saldo = 0
saldo_atualizado = 0
opcao = -1

valor_depositado = 0
valor_indicado_saque = 0

depositos = []  # Lista para armazenar todos os depósitos
saques = [] # Lista para armazenar todos os saques

limite_saques = 3  # Limite máximo de saques permitidos
contagem_saques = 0  # Contador de saques realizados

limite_transacoes = 10  # Limite máximo de transações diárias (depósitos + saques)
contagem_transacoes = 0  # Contador de transações realizadas

while opcao != 0:
        # Verifica se já foi atingido o limite de transações diárias
        if contagem_transacoes >= limite_transacoes:
            print("Limite de transações diárias atingido! Não é possível realizar mais transações hoje.")
            break
        # Menu
        opcao = int(input("[1] depositar \n[2] sacar \n [3] extrato \n [0] sair: "))

        if opcao == 1:
               deposito = float(input("Informe o valor a ser depositado:"))
               if deposito > 0:
                saldo_atualizado += deposito
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura data e hora
                depositos.append((deposito, data_hora))  # Armazena o depósito com data e hora
                depositos.append(deposito)  # Armazena o depósito na lista
                valor_depositado = sum(d[0] for d in depositos if isinstance(d, tuple)) # Atualiza valor depositado
                contagem_transacoes += 1  # Incrementa o contador de transações
                print(f"Valor de R$ {deposito:.2f} depositado com sucesso!")
               else:
                print("O valor depositado é inválido, tente novamente!")

        elif opcao == 2:
               # Verifica se já foram realizados 3 saques
               if contagem_saques >= limite_saques:
                   print("Limite de saques atingido! Não é possível realizar mais saques.")   
               else:
                   saque = float(input("Informe o valor desejado para saque: "))
                   #valor_indicado_saque = saque
                   saldo_pos_saque = saldo_atualizado - saque
                   if saque > 0:
                       #valor_a_sacar = saque
                       print("Aguarde, validando operação...")
                       if saldo_pos_saque > 0:
                           saldo_atualizado -= saque
                           data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura data e hora
                           saques.append(saldo_pos_saque) #Armazena o saque na lista
                           contagem_saques += 1  # Incrementa o contador de saques
                           contagem_transacoes += 1  # Incrementa o contador de transações
                           #valor_sacado = sum(saques) # Atualiza o valor total dos saques
                           #contagem_saques += 1  # Incrementa o contador de saques
                           print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
                       else:
                           print("Saldo insuficiente. Tente novamente!")
                   else:
                       print("Valor de saque inválido.")

        elif opcao == 3:
                print("\n=== Extrato da Conta ===")

                # Garantir que todos os elementos de 'depositos' sejam tuplas antes de iterar 
                depositos = [(d, "N/A") if isinstance(d, float) else d for d in depositos]
                saques = [(s, "N/A") if isinstance(s, float) else s for s in saques]  # Verifica e corrige a lista de saques

                if len(depositos) == 0 and len(saques) == 0:
                    print("Não foram realizadas transações.")
                else:
                    print("Depósitos:")
                    for valor, data_hora in depositos:
                        print(f"R$ {valor:.2f} em {data_hora}")

                    print("\nSaques:")
                    for valor, data_hora in saques:
                        print(f"R$ {valor:.2f} em {data_hora}")

                    print(f"Saldo atual: R$ {saldo_atualizado:.2f}")
        
        elif opcao == 0:
            break
        else:
            print("Operação Inválida, por favor, selecione novamente a opção desejada.")
                
               
print("Sessão encerrada.")