#Exercicio 4:Strings 
#1Peça uma frase e imprima: quantos caracteres tem, ela toda em maiusculas, e ela invertida.
texto=input( "Digite uma frase :")
print(f"Maiusculas:{texto.upper()},Tamanho:{len(texto)},Invertida:{texto[::-1]}")

#2.Conte quantas palavaras há numa frase .

frase= "O Jovem ficou insatisfeito"
lista_de_palavras = frase.split()
print(f"Tamanho da frase {frase} :{len(lista_de_palavras)}")

