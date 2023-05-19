#Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
#sua idade exata (em anos).

def main():
    dianascimento = int(input("Digite o dia em que você nasceu: "))
    mesnascimento = int(input("Digite o mês em que você nasceu: "))
    anonascimento = int(input("Digite o ano em que você nasceu: "))

    diahoje = int(input("Digite o dia, da data de hoje: "))
    meshoje = int(input("Digite o mes, da data de hoje: "))
    anohoje = int(input("Digite o ano, da data de hoje: "))

    idade = calcular_idade(dianascimento,mesnascimento,anonascimento,diahoje,meshoje,anohoje)

    print(f"Sua idade é de {idade} anos")

def calcular_idade(dianascimento,mesnascimento,anonascimento,diahoje,meshoje,anohoje):

    idade = anohoje - anonascimento-1

    if meshoje> mesnascimento:
        idade = idade + 1
        return idade
    elif meshoje == mesnascimento:
        if diahoje >= dianascimento:
            idade = idade + 1
            return idade
    else: idade = idade
    return idade

main()