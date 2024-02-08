# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

n = 13

def verifica_numero_fibonacci(n):
  if (n == 1):
    return "O número pertence a sequência de Fibonacci."
  
  ultimo = 1
  penultimo = 1
  
  while ultimo < n:
    numero = ultimo + penultimo
    penultimo = ultimo
    ultimo = numero

  if (n == ultimo):
    return "O número pertence a sequência de Fibonacci."
  else:
    return "O número NÃO pertence a sequência de Fibonacci."
  
mensagem = verifica_numero_fibonacci(n)
print(mensagem)