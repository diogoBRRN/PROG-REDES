n = int(input('Digite uma quantidade de fatores primos que o(s) número(s) em questão deve ter: '))
 
consecutivos = 0 #Contador que será incrementado sempre que um número tiver exatamente n fatores primos diferentes, tipo 2, 3 ,5 7 .....
comeco = 0 # contador que guardara o primeiro número da sequência quando a condição for satisfeita.

for numero in range(2, 99999): #Verifica todos os números de 2 até essse número gigante, procuramos os primeiros n (número escolhido pelo usuário) números consecutivos que tenham também n fatores primos diferentes.
   num_temp = numero #criamos uma cópia do número para fatorar, sem perder o valor original dele. Basicamente criamos outra variável para fazer as operações.
   cont = 0 #conta quantos fatores primos distintos o número atual possui 
   i = 2 # inicializa o possível divisor, como todos números são divisiveis por 1, a gente começa do 2.

   for i in range(2, numero + 1): # aqui é um loop para fatorar a variável número temporária que criamos. (AQUI TESTAMOS TODOS OS DIVISORES DE 2 ATÉ O NÚMERO)
      if (i * i) > num_temp: 
         break
      if num_temp % i == 0: 
         cont+=1
         while num_temp % i == 0:
            num_temp //= i
   
   if num_temp > 1:
      cont += 1

   if cont == n: 
      consecutivos += 1
      if consecutivos == n:
         comeco = numero - n + 1
         break
   else:
     consecutivos=0

for x in range(n):
   print(comeco + x)
