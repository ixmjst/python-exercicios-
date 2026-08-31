# Exercicio 2 : Condicionais (if/elif/else )
# Peça um número e diga se é positivo , negativo ou zero

numero=int(input(" Digite um numero:"))
if(numero>0):
    print("Positivo")
elif(numero<0):
    print("Negativo")
else:
    print("Igual a 0")

# 2.Peça uma nota de 0 a 20 e classifique: reprovado,suficiente , bom ou excelente.
nota=float(input(" Digite uma nota de 0-20: "))
if(nota>16):
        print("Excelente")        
elif((nota>=13)and (nota<=16)):
        print("Bom")     
elif((nota>=10)and(nota<=12)):
        print("Suficiente")     
else:
        print("Reprovado")

#3.Imprimir "processando" se a var texto não estiver vazia e uma variavel de click for verdadeira.

texto=""
click=33
texto=input("Digite um texto qualquer:")
if ((texto!="")and (click)):
    print("\bProcessando...")
else:
    print("nada para mostrar")

