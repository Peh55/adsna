#1.

# metros = float(input("Digite o numero em metros: "))

# centimetros = metros * 100

# print(f"total de {centimetros} cm.")

#3.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

diferenca = 0

mostra_msg = True # Variavel do tipo booleana = True ou False


if num1 > num2:
    diferenca = num1 - num2

elif num2 > num1:
    diferenca = num2 - num1

else:
    print("não ha diferença entre os dois")
    mostra_msg = False

if mostra_msg:
    print(f"a diferença entre os dois é: {diferenca}")

#quando se trabalha com programação tem um conceito importante que é o escopo, o escopo local e o escopo global