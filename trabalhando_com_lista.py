lista = ['Python', 'PHP', 'SQL', 'HTML']

print(lista[1])

print('---------------------')

print(f"A lista iniciou com {len(lista) } itens.")


print("Minha Lista")
print(lista)

print('---------------------')
print(f"A lista esta no tipo {type(lista)}")

print('---------------------')

add = input("Digite uma linguagem de programação: ")

#a linha abaixo adiciona no final da lista
lista.append(add)

print("Lista com novo item")
print(lista)


print('---------------------')
inserir_na_posicao2 = input("Digite o que você vai adicionar: ")

lista.insert(2, inserir_na_posicao2)

print("Lista com o novo item na posicao 2")
print(lista)

print('---------------------')
print(f"Quantidade de itens em uma lista {len(lista) }")

print('---------------------')

excluir = input("informe a posicao do item que deseja excluir: " -1)
lista.pop(excluir)


print(lista)