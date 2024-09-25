#ENTRADA DE DADOS 
nome = input('Digite o nome do funcionário: ')
sal_bruto = float(input('Digite o salario bruto: R$ '))

#PROCESSAMENTO DE DADOS 
VA = sal_bruto * 0.05
INSS = sal_bruto * 0.11

total_desconto = VA + INSS

sal_liq = sal_bruto - (VA + INSS)
#SAÍDA DE DADOS 

print(f"{nome} seu salário liquido é R$ {sal_liq}")

print(f"Total de desconto R${total_desconto}")