#Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
#obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

def main():
    angulo1 = int(input("Digite o angulo 1: "))
    angulo2 = int(input("Digite o angulo 2: "))
    angulo3 = int(input("Digite o angulo 3: "))

    tipo_de_triangulo =classificar_triangulo(angulo1,angulo2,angulo3)

def eh_triangulo(angulo1,angulo2,angulo3):
    if((angulo1+angulo2+angulo3)==180 and angulo1!=0 and angulo2 !=0 and angulo3 !=0):
        return True
    else:
        return False

def classificar_triangulo(angulo1,angulo2,angulo3):
    if eh_triangulo(angulo1,angulo2,angulo3):
        if(angulo1==90 or angulo2==90 or angulo3==90):
            print(f"O triangulo é retângulo")
        elif(angulo1>90 or angulo2>90 or angulo3>90):
            print(f"O triângulo é obtsusângulo")
        else:
            print("O triângulo é acutângulo")
    else:
        print(f"Os ângulos não formam um triângulo!")






main()