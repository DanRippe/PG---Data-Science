import numpy as np
import pandas as pd
import collections
import random

print("--- Medidas de posição em Python ---")

# Dados de exemplo: Pontuações em um jogo (de 0 a 100)
pontuacoes = [85, 92, 78, 88, 95, 70, 80, 90, 85, 75, 92, 85, 60, 99, 88]

# convertendo para uma Series do Pandas para facilitar os cálculos
sPontuacoes = pd.Series(pontuacoes)

# 1. Média Aritmética
mediaPontuacoes = sPontuacoes.mean()
print(f"\n1. Média das pontuações: {mediaPontuacoes:.2f}")

# 2. Mediana
medianaPontuacoes = sPontuacoes.median()
print(f"2. Mediana das pontuações: {medianaPontuacoes:.2f}")

# 3. Moda
# collections.Counter é útil para encontrar a moda, principalmente se houver múltiplas modas
contagemPontuacoes = collections.Counter(pontuacoes)
# A(s) moda(s) são os valores com a maior contagem
maxFrequencia = max(contagemPontuacoes.values())
modas = [valor for valor, frequencia in contagemPontuacoes.items() if frequencia == maxFrequencia]

if len(modas) == len(pontuacoes):   #todos os valores aparecem uma vez
    print("3. Moda das pontuações: Nenhuma moda (todos os valores são únicos)")
elif len(modas) > 1:
    print(f"3. Moda das pontuações (bimodal/multimodal): {modas}")
else:
    print(f"3. Moda das pontuações: {modas[0]}")

# 4. Quartis e Percentis
q1 = sPontuacoes.quantile(0.25)
q2 = sPontuacoes.quantile(0.5)  # Mediana
q3 = sPontuacoes.quantile(0.75)
p90 = sPontuacoes.quantile(0.9) # 90% Percentil

print(f"\n4. Quartis e Percentis:")
print(f"    Primeiro Quartil (Q1 - 25%): {q1:.2f}")
print(f"    Segundo Quartil (Q2 - 50% - Mediana): {q2:.2f}")
print(f"    Terceiro Quartil (Q3 - 75%): {q3:.2f}")
print(f"    90% Percentil (P90): {p90:.2f}")

# O método describe() do Pandas mostra várias dessas medidas juntas
print("\nResumo das medidas de posição (e dispersão) com .describe():")
print(sPontuacoes.describe())

print("\n--- Introdução à Probabilidade em Python (Simulação) ---")

# 1. Lançamento de uma moeda
# Espaço Amostral: {'Cara', 'Coroa'}
# Evento: Obter 'Cara'
numLancamentos = 1000 # Quantas vezes vamos lançar a Moeda
resultados = []

for i in range(numLancamentos):
    resultado = random.choice(['Cara', 'Coroa'])
    resultados.append(resultado)

# Contar a frequência de 'Cara'
contagemCaras = resultados.count('Cara')
probabilidadeCaraSimulada = contagemCaras / numLancamentos

print("\n1. Lançamento de moeda (simulação)")
print(f"Número de lançamentos: {numLancamentos}")
print(f"Número de 'Caras' obtidas: {contagemCaras}")
print(f"Probabilidade simulada de 'Cara': {probabilidadeCaraSimulada:.2f} (Esperado: 0.50)")
print("Quanto maior o número de lançamentos, mais a probabilidade simulada se aproxima da teórica")
print("(Lei dos Grandes Números)")

# 2. Rolagem de um Dado
# Espaço Amostral: {1, 2, 3, 4, 5, 6}
# Evento: Obter um número par ({2, 4, 6})
numRolagens = 1000 # Quantas vezes vamos lançar o Dado
resultadosDado = []

for i in range(numRolagens):
    resultado = random.randint(1, 6) # Simula a rolagem de um dado de 6 faces
    resultadosDado.append(resultado)

# Contar quantos resultados são pares
contagemPares = sum(1 for num in resultadosDado if num % 2 == 0)
probabilidadeParSimulada = contagemPares / numRolagens

print("\n2. Rolagem de Dado (Simulação)")
print(f"Número de Rolagens: {numRolagens}")
print(f"Número de resultados pares: {contagemPares}")
print(f"Probabilidade simulada de obter um número par: {probabilidadeParSimulada:.2f} (esperado: 0.50)")