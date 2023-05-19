#Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
def main():
    numero1 = int(input("Digite o número 1: "))
    numero2 = int(input("Digite o número 2: "))
    numero3 = int(input("Digite o número 3: "))

    numiguais = verificar_igualdade(numero1,numero2,numero3)
    print(f'Você digitou {numiguais} número(s) iguais.')

def verificar_igualdade(num1,num2,num3):
    if(num1 == num2 == num3):
     return 3
    elif((num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2) or (num2 == num3 and num1 != num2)):
     return 2
    else:
     return 0







main()