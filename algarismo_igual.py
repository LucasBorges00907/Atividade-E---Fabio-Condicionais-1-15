#Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou 
#diferente do algarismo da unidade.
def main():
    numero1 = float(input("Digite o número : "))
    igual = verificar_igualdade(numero1)

def verificar_igualdade(numero1):
    dezenas = numero1//10
    unidades = numero1%10
    if (dezenas==unidades):
        print(f"O algarismo das dezenas é igual ao das unidades")
    else:
        print(f"O algarismo das dezenas é diferente do das unidades")










main()