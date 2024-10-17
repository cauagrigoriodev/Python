#Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo.
#Observação – Para formar os lados de um triângulo cada um dos valores tem que ser menor que a soma dos outros dois.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))

if ( n1 + n2 ) > n3 or ( n2 + n3) > n1 or (n3 + n1) >n2:
    print("Esses numeros podem formar um triângulo")
else:
    print("Os numeros que você colocou não forma um triângulo")    
    