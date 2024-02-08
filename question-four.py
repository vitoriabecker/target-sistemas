# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
# que cada estado teve dentro do valor total mensal da distribuidora.

faturamento_por_estado = {'SP' : 67836.43, 'RJ' : 36678.66, 'MG' : 29229.88, 'ES' : 27165.48, 'Outros' : 19849.53}

def calcula_percentual_faturamento(faturamento_por_estado):
  faturamento_total = sum(faturamento_por_estado.values())
  percentual_faturamento_por_estado = {}

  for estado, faturamento in faturamento_por_estado.items():
    percentual_faturamento = (faturamento/faturamento_total) * 100
    percentual_faturamento_por_estado[estado] = percentual_faturamento
  
  return percentual_faturamento_por_estado

percentual_por_estado = calcula_percentual_faturamento(faturamento_por_estado)

for estado, percentual in percentual_por_estado.items():
  print(f'O estado de {estado} obteve um percentual de representação de {percentual:.2f}%.')




