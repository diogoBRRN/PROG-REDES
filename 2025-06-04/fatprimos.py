n = int(input('Digite uma quantidade de fatores primos que o(s) número(s) em questão deve ter: '))
 
consecutivos = 0 #Contador que será incrementado sempre que um número tiver exatamente n fatores primos diferentes, tipo 2, 3 ,5 7 .....
comeco = 0 # contador que guardara o primeiro número da sequência quando a condição for satisfeita.

for numero in range(2, 99999): #Verifica todos os números de 2 até essse número gigante, procuramos os primeiros n (número escolhido pelo usuário) números consecutivos que tenham também n fatores primos diferentes.
   num_temp = numero #criamos uma cópia do número para fatorar, sem perder o valor original dele. Basicamente criamos outra variável para fazer as operações.
   cont = 0 #conta quantos fatores primos distintos o número atual possui 
   i = 2 # inicializa o possível divisor, como todos números são divisiveis por 1, a gente começa do 2.

   for i in range(2, numero + 1): # aqui é um loop para fatorar a variável número temporária que criamos. (AQUI TESTAMOS TODOS OS DIVISORES DE 2 ATÉ O NÚMERO)
      if (i * i) > num_temp: #testamos todos os divisores posssíveis de numtemp de uma forma mais rápida de modo que se i*i>num_temp já testamos todos os possíveis divisores primos menores que a raiz de numero temporario.
         break
      if num_temp % i == 0: #se i divide num_temp e o resto é zero ele é um fator primo
         cont+=1 #conta o fator primo diferente
         while num_temp % i == 0:
            num_temp //= i #divide num_temp repetidas vezes ( até o resto ficar 0) por i e pega sua parte inteira. O objetivo aqui é remover as cópias 
                           # (potências de um mesmo fator) da fatoração.
   
   if num_temp > 1: #se depois do loop sobrou um numero maior que 1, ele também é um fator primo (é primo por si só). conta +1
      cont += 1

   if cont == n: #se o numero atual tem exatamente n fatores primos distintos (numero q a gente pediu).
      consecutivos += 1 #incrementa numero de consecutivos
      if consecutivos == n:
         comeco = numero - n + 1 #calcula o inicio da sequencia
         break
   else:
     consecutivos=0

for x in range(n):
   print(comeco + x)
