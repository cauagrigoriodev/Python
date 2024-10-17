# Execicio Python 


nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite outra nota: "))
nota3 = int(input("Digite mais uma nota: "))

if nota1 > nota2 and nota1 > nota3:
    print(f"A nota maior das tres é: {nota1}")
elif nota2 > nota1 and nota2 > nota3:
    print(f"A nota maior das tres é: {nota2}")
elif nota3 > nota1 and nota3 > nota2:
    print(f"A nota maior das tres é: {nota3}")
else:
    print("Contém duas ou mais notas iguais")
