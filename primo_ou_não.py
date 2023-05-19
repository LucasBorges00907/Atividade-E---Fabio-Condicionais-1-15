def main():
    numero = int(input("Digite um número de 1 a 100: "))
    
    eh_primo(numero)

   



def eh_primo(numero):
    if numero == 0 or numero == 1:
        print("O número não é primo!")
    elif numero % 2 != 0 or numero % 3 != 0 or numero % 5 != 0 or numero % 7 != 0 or numero % 11 != 0 or numero % 13 != 0:
        print("O número é primo!")
    else:
        print("O número não é primo!")






main()