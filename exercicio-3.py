# Exercicio 3: Laços (for e while)
#1.Imprima os números de 1  a 10 com um for. Depois só os pares .

for i in range(1,10):
    print(i)
   
for j in range(1,10):
     par=f"{j}"if (j%2==0) else "numero impar"
     print(par)
