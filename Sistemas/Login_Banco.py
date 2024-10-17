# inicalização do sistema 
# colocando as informações dos clientes
print("Informe os dados solicitados abaixo")
clientes = input("Digite seu nome: ")
#função de validação se o cpf está recendo somente numeros 
def login():
    while True:
        cpf = input("Digite seu CPF (somente numeros): ")
        if cpf.isdigit() and len(cpf) == 11: #limte padrão de algoritimos 
            break
        elif cpf.isdigit() and len(cpf) < 11 or cpf.isdigit() and len(cpf) > 11:
            print("Por Favor digite um cpf válido!")
        else:
            print("Digite somente numeros!")    

login()
#Função para validar conta bancaria 
def entrar_contabank():
    while True:
        id_conta = input("Digite o número da sua conta bancária: ")
        if id_conta.isdigit() and len(id_conta) == 6:  # Supondo que a conta tenha 6 dígitos
            print(f"Olá {clientes},Bem-vindo ao Banco Inter!")
            break
        else:
            print("O número da conta bancária está errado. Tente novamente.")

entrar_contabank()
