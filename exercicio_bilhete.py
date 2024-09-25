bilhete = input("""
Em qual dessas opções se encaixa:
 -(E) - estudante
 -(I) - idoso
 -(O) - outro
                

Informe a opção desejada:""").upper()

valor = float(input("digite o valor do ingresso:"))

meia = valor * 0.50

idoso = valor * 0

if bilhete == "idoso":
    print(f"ingresso gratuito{idoso}")
elif bilhete == "estudante":
    print(f"o valor a pagar é{meia}")
else:
    print(f"o valor a pagar é{valor}")