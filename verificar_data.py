def main():
    dia = int(input("Digite o dia da data: "))
    mes = int(input("Digite o mês da data: "))
    ano = int(input("Digite o ano da data: "))

    DataValida = verificar_data(dia,mes,ano)

def verificar_data(dia,mes,ano):
      if dia > 0 and mes > 0:
           if dia > 31 or mes>12:
                print("Inválida")
           else:
                print("Válida")   
      else:
           print("Inválida")
           
       

        







main()