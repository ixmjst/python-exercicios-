#Exercicio 5:
# 1. Crie uma lista de compras . Adicione itens com .append(), remova um, e imprima a lista final e seu tamanho
lista_compras=["arroz", "feijao","batata","banana","sapado","bolsa"]
lista_compras.append("Manteiga")
lista_compras.remove("arroz")
#2. Percorra a lista com for e enumere cada item da lista
print("Lista Final:")
for indice, compra in enumerate(lista_compras,1):
    print(indice,compra)

print(f"Tamanho da Lista:{len(lista_compras)}")
