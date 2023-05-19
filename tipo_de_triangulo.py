#Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
#(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
#formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).
def main():
    lado1 = int(input("Digite o lado 1: "))
    lado2 = int(input("Digite o lado 2: "))
    lado3 = int(input("Digite o lado 3: "))
    triangulo = eh_triangulo(lado1,lado2,lado3)
    tipodetriangulo = definir_tipo_de_trangulo(lado1,lado2,lado3)


def eh_triangulo(lado1,lado2,lado3):
    if (lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1):
        print(f"Sim, esses lados formam um triângulo!")
    else:
        print(f"Não, esses lados não formam um triângulo!")
    
def definir_tipo_de_trangulo(lado1,lado2,lado3):
    if (eh_triangulo):
        if(lado1==lado2==lado3):
            print(f"O triângulo é equilátero!")
        elif(lado1!=lado2 and lado1!=lado3 and lado3!=lado2 ):
            print(f"O triângulo é escaleno!")
        else:
            print(f"O triângulo é isósceles!")
    
        

        








main()