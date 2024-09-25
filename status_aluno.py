nome = input("Digite seu nome:")

nota1 = float(input("Digite sua 1ª nota: "))

nota2 = float(input("Digite sua 2ª nota: "))

freq = float(input("Digite a frequecia em aula: "))

media = (nota1 + nota2) / 2

if media >= 6.0 and freq >= 75.0:
    print(f"{nome} sua média é {media}, você esta APROVADO")
else:
    print(f"{nome} sua média {media}, você esta REPROVADO")