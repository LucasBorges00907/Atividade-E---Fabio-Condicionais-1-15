#Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

def main():
    
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))
    opcao = int(input('Digite a sua opção (1, 2 ou 3): '))
    
    verificar_opcao(opcao, num1, num2, num3)
    
    
def verificar_opcao(opcao, num1, num2, num3):
    if opcao == 1:
        print(f'O numero escolhido foi {num1}.')
    elif opcao == 2:
        print(f'O numero escolhido foi {num2}.')
    elif opcao == 3:
        print(f'O numero escolhido foi {num3}.')
    else:
        print('Você não escolheu uma opção válida.')



main()