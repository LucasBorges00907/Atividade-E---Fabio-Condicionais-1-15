#Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
#diferentes.
def main():
    numero1 = int(input('Digite o número 1: '))
    numero2 = int(input('Digite o número 2: '))
    numero3 = int(input('Digite o número 3: '))
    numero4 = int(input('Digite o número 4: '))
    numero5 = int(input('Digite o número 5: '))
    
    maior = verificar_maior(numero1, numero2, numero3, numero4, numero5)
    
    menor = verificar_menor(numero1, numero2, numero3, numero4, numero5)
    
    print(f'O maior número é {maior} e o menor é {menor}')


def verificar_maior(num1, num2, num3, num4, num5):
    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    if num4 > maior:
        maior = num4
    if num5 > maior:
        maior = num5
    return maior
    

def verificar_menor(num1, num2, num3, num4, num5):
    menor = num1
    if num2 < menor:
        menor = num1
    if num3 < menor:
        menor = num3
    if num4 < menor:
        menor = num4
    if num5 < menor:
        menor = num5
    return menor






main()