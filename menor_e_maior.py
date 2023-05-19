#Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
def main():
    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))
    maior = verificar_maior(numero1,numero2)
    menor = verificar_menor(numero1,numero2)
    print(f"O maior número é {maior} e o menor número é {menor}")

def verificar_maior(numero1,numero2):
    if numero1>numero2:
     return numero1
    else:
     return numero2
    
def verificar_menor(numero1,numero2):
    if numero1<numero2:
     return numero1
    else:
     return numero2

main()