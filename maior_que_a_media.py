#Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.
def main():
    numero1 = int(input('Digite o número 1: '))
    numero2 = int(input('Digite o número 2: '))
    numero3 = int(input('Digite o número 3: '))
    numero4 = int(input('Digite o número 4: '))
    numero5 = int(input('Digite o número 5: '))

    media = (numero1+numero2+numero3+numero4+numero5)/5
    print(f'A média desses números é {media} e os números acima da média são: ')
    acima_da_media(numero1,numero2,numero3,numero4,numero5,media)

def acima_da_media(numero1,numero2,numero3,numero4,numero5,media):
    if numero1 > media:
        print(f'{numero1}')
    if numero2 > media:
        print(f'{numero2}')
    if numero3 > media:
        print(f'{numero3}')
    if numero4 > media:
        print(f'{numero4}')
    if numero5 > media:
        print(f'{numero5}')



main()