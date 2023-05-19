#Leia 1 (um) número inteiro e escreva se este número é par ou impar.
def main():
    numero = int(input("Digite um número: "))
    eh_par(numero)


def  eh_par(numero):
    if numero%2==0:
         print("O número é par")
    else:
         print("O número é ímpar")
   
    
main()