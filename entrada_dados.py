#ENTRADA DE DADOS
#n = input(number())
n1 = int(input('Digite seu 1º número: '))
n2 = float(input('Digite seu 2º número: '))

#PROCESSAMENTO DE DADOS
soma = n1 + n2

subtracao = n1- n2

multiplicacao = n1 * n2 

divisao = n1 / n2

potencia = n1 ** 2

#SAÍDA DE DADOS
print("Soma = ", soma)
print("Subtração", subtracao)
print("Multiplicação", multiplicacao)
print("Divisao", divisao)
print(f"Potência de {n1}² = {potencia}")

#VERIFICANDO O TIPO DA VARIAVEL
print("A variavel n1 é do tipo: ", type(n1))

print("A variavel soma é do tipo: ", type(soma ))