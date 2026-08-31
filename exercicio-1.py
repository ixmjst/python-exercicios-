 #Exercicio 1 : Var, tipos e entrada / saida 
 #Peça o nome e a idadae do usuário com input() e imprima uma frase que combine os dois.
 # Calcular em  quantos anos a pessoa fará 100 anos .
nome = input("Digite o nome:").strip().lower()
idade= int(input(" Digite a idade:"))

print(f"Seu Nome:{nome}, e sua idade: {idade}.Em {100-idade} fara 100 anos")

