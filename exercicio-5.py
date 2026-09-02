#Exercicio 5:
# 1. Crie uma lista de compras . Adicione itens com .append(), remova um, e imprima a lista final e seu tamanho
lista_compras=["arroz", "feijao","batata","banana","sapato","bolsa"]
lista_compras.append("Manteiga")
lista_compras.remove("arroz")
maior=1
menor=1
#2. Percorra a lista com for e enumere cada item da lista
#3. Descubra o maior e o menor número de uma lista de números, sem usar max()/min() — na lógica, com um laço.
print("Lista Final:")
for indice, compra in enumerate(lista_compras,1):
     maior=indice
     if(indice>maior):
       maior=indice
     if(indice<menor):
       menor=indice
     print(indice,compra)
   
print(f"Tamanho da Lista:{len(lista_compras)}")
print("Maior: ",maior)
print("Menor: ",menor)
