# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

file = open("dados.json")
dados = json.load(file)

def get_menor_valor(dados):
  menor = dados[0].get('valor')

  for i in range(len(dados)):
    if dados[i].get('valor') < menor:
      menor = dados[i].get('valor')
    
  return menor
    
def get_maior_valor(dados):
  maior = dados[0].get('valor')

  for i in range(len(dados)):
    if dados[i].get('valor') > maior:
      maior = dados[i].get('valor')
    
  return maior

def get_superior_media(dados):
  valores = []
  for i in range(len(dados)):
    if (dados[i].get('valor') != 0):
      valores.append(dados[i].get('valor'))

  valor_total = sum(valores)
  media_mensal = valor_total/len(valores)

  maior_que_media = 0
  for i in range(len(valores)):
    if valores[i] > media_mensal:
      maior_que_media +=1
    
  return maior_que_media

menor_valor = get_menor_valor(dados)
print(f'Menor valor de faturamento no mês: R$ {menor_valor:.2f}')

maior_valor = get_maior_valor(dados)
print(f'Maior valor de faturamento no mês: R$ {maior_valor:.2f}')

dia_superior_media = get_superior_media(dados)
print(f'Quantidade de dias em que o faturamento foi superior ao da média mensal: {dia_superior_media}')