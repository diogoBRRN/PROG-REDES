# Solicita os números inteiros positivos ao usuário
num1 = int(input("Digite o primeiro número inteiro positivo: "))
num2 = int(input("Digite o segundo número inteiro positivo: "))

a = num1
b = num2

# Enquanto b não for zero, realiza o cálculo do MDC. Quando B se tornar zero A vira o MDC. Pois todo número divide 0.
for _  in range(10000000000000000):
  
    if b == 0: #Quando b == 0, significa que encontramos o mdc
          break
  
    temp = a % b # pegamos o resto da divisão de a por b e guardamos em temp, depois esse valor é jogado pro b. 
                 # O objetivo é ficar dividindo até b (temp) se tornar zero.
 
    a = b # A vai receber o valor de B, que consequentemente será o MDC "provisório" a cada divisão, 
          #quando B (temp) se tornar zero chegamos ao mdc, e esse último valor encontrado vai pra variável A (que é o MDC).

    b = temp #atualiza o valor de B
   


# Quando b se torna zero, o valor de "a" é o MDC
print("O Máximo Divisor Comum (MDC) de", num1, "e", num2, "é:", a)
