# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = 'Memento 2000'

def inverter_string(string):
  reverse_string = ""
  for char in range(len(string)):
    reverse_string += string[-(char+1)]

  return reverse_string

reverse_string = inverter_string(string)
print(reverse_string)

# Outra forma mais simples, mas com menos lógica
def inverter_string(string):
  return string[::-1]

reverse_string = inverter_string(string)
print(reverse_string)

