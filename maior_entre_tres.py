#Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
def main():
    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))
    numero3 = float(input("Digite o número 3: "))
    maior = verificar_maior(numero1,numero2,numero3)
    print(f"O maior número entre os 3 é {maior}")
    

def verificar_maior(numero1,numero2,numero3):
    if (numero1>numero2 and numero1>numero3):
        return numero1
    elif(numero2>numero1 and numero2>numero3):
        return numero2
    else:
        return numero3
     
    



main()