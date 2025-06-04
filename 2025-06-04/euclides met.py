# Solicita os números inteiros positivos ao usuário
num1 = int(input("Digite o primeiro número inteiro positivo: "))
num2 = int(input("Digite o segundo número inteiro positivo: "))

a = num1
b = num2

# Enquanto b não for zero, realiza o cálculo do MDC. Quando B se tornar zero A vira o MDC. Pois todo número divide 0.
while b != 0:
    # Calcula o resto da divisão de a por b e guarda em uma variável temporária.
    #  Esse é o passo fundamental do algoritmo: ele se baseia na propriedade de que os divisores comuns de a e b são os mesmos dos números b e a % b
    # Por exemplo, se tivermos dois números (a, b), o MDC(a, b) é igual a MDC(b, a % b).
    temp = a % b
    # Atualiza os valores: "a" recebe o valor de "b" 
    a = b
    # "b" recebe o valor do resto obtido
    b = temp
       #Essencialmente, estamos substituindo o par original (a, b) por (b, a % b). 
       # Essa substituição é repetida iterativamente, o que "reduz" os números até que o resto se torne zero. 
       # A cada iteração, o par é modificado, mas a propriedade fundamental do MDC é preservada (que é o resto se tornar zero).



# Quando b se torna zero, o valor de "a" é o MDC
print("O Máximo Divisor Comum (MDC) de", num1, "e", num2, "é:", a)
