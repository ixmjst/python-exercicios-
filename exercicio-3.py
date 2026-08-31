# Exercicio 3: Laços (for e while)
#1.Imprima os números de 1  a 10 com um for. Depois só os pares .

for i in range(1,10):
    print(i)
   
for j in range(1,10):
     par=f"{j}"if (j%2==0) else "numero impar"
     print(par)

# 2. Some todos os  números de 1 a 100 usando um laço e uma variável acumuladora
soma =0
for k in range(1,100):
    soma=soma+k

print(f"Soma:{soma}")

# 3. Peça senhas ao usuário repetidamente com um while até ele digitar a correta 
senha = 1234
valor=int(input("Digite a senha: "))
while(valor!=senha):
   valor=int(input("Digite a senha: "))

print("Acesso Aprovado!")