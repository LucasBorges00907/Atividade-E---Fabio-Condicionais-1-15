#Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.

def main():
    valorporhora1 = float(input("Digite o valor por hora recebido pelo professor 1:"))
    numerodehoras1 = int(input("Digite o número de horas trabalhadas pelo professor 1:"))
    valorporhora2 = float(input("Digite o valor por hora recebido pelo professor 2:"))
    numerodehoras2 = int(input("Digite o número de horas trabalhadas pelo professor 2:"))

    salario1 = valorporhora1*numerodehoras1
    salario2 = valorporhora2*numerodehoras2
    maior_salario(salario1,salario2)

def maior_salario(salario1,salario2):
    if salario1 > salario2:
        print("O professor 1 tem o salário total maior")
    else:
        print("O professor 2 tem o salário total maior")

main()