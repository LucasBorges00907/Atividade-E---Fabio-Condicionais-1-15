#Leia 3 (três) números e escreva-os em ordem crescente.
def main():
    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))
    numero3 = float(input("Digite o número 3: "))
    ordemcrescente = verificar_ondem_crescente(numero1,numero2,numero3)


def verificar_ondem_crescente(num1,num2,num3):
    if  num1 > num2 and num2 > num3:
        ordem = num3, num2, num1
    elif num1 > num3 and num3 > num2:
        ordem = num2, num3, num1
    elif num2 > num3 and num3 > num1:
        ordem = num1, num3, num2
    elif num2 > num1 and num1 > num3:
        ordem = num3, num1, num2
    elif num3 > num2 and num2 > num1:
        ordem = num1, num2, num3
    else:
        ordem = num2, num1, num3
    
    return ordem



