#Exercicio 4:Strings 
#1Peça uma frase e imprima: quantos caracteres tem, ela toda em maiusculas, e ela invertida.
texto=input( "Digite uma frase :")
print(f"Maiusculas:{texto.upper()},Tamanho:{len(texto)},Invertida:{texto[::-1]}")

#2.Conte quantas palavaras há numa frase .

frase= "O Jovem ficou insatisfeito"
lista_de_palavras = frase.split()
print(f"Tamanho da frase {frase} :{len(lista_de_palavras)}")

#3.Limpe um texto bagunçado: troque quebras de linha por espaçoes e remova espaços duplicados 
texto_exemplo=f"""
 Ola eu sou o Paulo e estou muito feliz por ver você
 Nossa amizade sera muito boa e proveitosa porque gosto de tecnologia e tu tambem.
 Odeio ficar sem fazer nada.
"""
#junta tudo novamente usando apenas um espaço.
print(" ".join(texto_exemplo.replace("\n"," ").split()))