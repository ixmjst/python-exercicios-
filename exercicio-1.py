 #Exercicio 1 : Var, tipos e entrada / saida 
 #1.Peça o nome e a idadae do usuário com input() e imprima uma frase que combine os dois.
nome = input("Digite o nome:").strip().lower()
idade= int(input(" Digite a idade:"))
print(f"Seu Nome:{nome}, e sua idade: {idade}.")
 # 2.Calcular em  quantos anos a pessoa fará 100 anos . Mostre o resultado numa frase
print(f"Em {100-idade} fara 100 anos ")
#3.Crie variáveis com seu tipo: um texto (str), um inteiro (int), um decimal (float) e um
#verdadeiro/falso (bool). Imprima o type() de cada uma para ver os nomes que o Python dá a eles
texto ="ola, malta "
inteiro=23
decimal=34.3
verdadeiro=False 
print(f"Texto:{type(texto)},\nInterio:{type(inteiro)},\nDecimal:{type(decimal)},\nBooleano:{type(verdadeiro)}")

