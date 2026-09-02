#Exercicio 6:
#1. Crie um dicionário representando um colaborador : nome, cargo, departamento.Imprima cada campo
colaborador={"nome":"jose","cargo":"IT manager","departamento":"IT"}

for key,value  in colaborador.items():
     print(key+":"+value)    
     
#2.Faça uma lista de vários colaboradores (cada um um dicionário) e percorra imprimindo só os nomes.
lista_colaboradores=[{"nome":"jose","cargo":"IT manager","departamento":"IT"},{"nome":"Maria","cargo":"IT manager","departamento":"IT"},{"nome":"Marcos","cargo":"IT manager","departamento":"IT"}]
print("Imprimindo apenas o nome:")
for value in lista_colaboradores:
    print(value["nome"])

#3. Conte a frequência de cada palavra numa frase, guardando o resultado num dicionário.
