# inicalização do sistema 
# colocando as informações dos clientes
print("Informe os dados solicitados abaixo")
clientes = input("Digite seu nome: ")
def login():
    while True:
        cpf = input("Digite seu CPF: ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        elif cpf.isdigit() and len(cpf) < 11 or cpf.isdigit() and len(cpf) > 11:
            print("Por Favor digite um cpf válido!")
        else:
            print("Digite somente numeros!")    

login()
def entrar_contabank():
    while True:
        id_conta = input("Digite o número da sua conta bancária: ")
        if id_conta.isdigit() and len(id_conta) == 6:  # Supondo que a conta tenha 6 dígitos
            print(f"Olá {clientes},Bem-vindo ao Banco Inter!")
            break
        else:
            print("O número da conta bancária está errado. Tente novamente.")

entrar_contabank()
