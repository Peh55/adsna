valor_pagar = float(input("Digite o valor total da compra: "))

forma_pgto = input("""
Escolha a forma de pagamento:
 - (B) = Boleto
 - (C) = Crédito
 - (D) = Débito
 - (PIX) = PIX
 - (DI) = Dinheiro

 Informe a opção desejada: """).upper()

if forma_pgto == "B" or forma_pgto == "DI":

    valor_pagar = valor_pagar * 0.85
    print(f"como o desconto de 15%, o valor ficou {valor_pagar}")

elif forma_pgto == "C":
    parcelar = input('Deseja parcelar? (S) Sim | (N) Não:').lower()

    if parcelar ==  "s":
        num_parcela = int(input("Informe a quantidade de parcelas: "))
        valor_parcela = round(valor_pagar / num_parcela, 2)

        print(f"""valor total = R$ {valor_pagar}
Valor de parcela + R$ {valor_parcela}
Quantidade de parcelas: {num_parcela} """)
        
    elif parcelar == 'n':
        print(f"total a pagar = R$ {valor_pagar}")

    else:
        print("Opção de parcela inválida!!!")

elif forma_pgto == 'D' or forma_pgto == 'PIX':
    valor_pagar = valor_pagar * 0.95
    print(f"Valor a pagar R$ {valor_pagar}")

else:
    print("Opção inválida!!!")




#dontpad.com/ads1na