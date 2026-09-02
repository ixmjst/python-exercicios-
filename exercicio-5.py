#Exercicio 5:
# 1. Crie uma lista de compras . Adicione itens com .append(), remova um, e imprima a lista final e seu tamanho
lista_compras=["arroz", "feijao","batata","banana","sapado","bolsa"]
lista_compras.append("Manteiga")
lista_compras.remove("arroz")
print("Lista Final:")
for compra in lista_compras:
    print(compra)

print(f"Tamanho da Lista:{len(lista_compras)}")