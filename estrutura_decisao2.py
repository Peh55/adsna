valor_pagar = float(input("Digite o valor total da compra: "))

forma_pgto = input("""
Escolha a forma de pagamento:
 - (B) = Boleto
 - (C) = Cartão
 - (D) = Dinheiro
 - (E) = pix

 Informe a opção desejada: """).upper()

if forma_pgto == "B":

    valor_pagar = valor_pagar * 0.85
    print(f"Com desconto de 15%, o valor ficou {valor_pagar}")

elif forma_pgto == "C":
    print("você optou pagar em CARTÃO")

elif forma_pgto == "D":
    print("você optou pagar em DINHEIRO")

elif forma_pgto == "E":
    print("você optou pagar em PIX")

else:
    print("forma de pagamento não identificada")

if forma_pgto == "B":   

    print(f"você digitou = {forma_pgto}")

elif forma_pgto == "C":

    print(f"você digitou = {forma_pgto}")

elif forma_pgto == "D":

    print(f"você digitou = {forma_pgto}")

elif forma_pgto == "E":

    print(f"você digitou = {forma_pgto}")

else:
    print(f"você digitou = {forma_pgto}")
    print("escolha uma forma de pagamento")