import numpy as np
import random

print("--- Simulação de um Modelo de Markov ---")

# 1. Definir os Estados
estados = ['Sol', 'Nublado', 'Chuva']
print(f"Estador possíveis do tempo: {estados}")

# 2. Definir a Matriz de Transição
# As linhas somam 1.0 (probabilidades de sair de um estado)
# Matriz de Transição (probabilidade de ir de [linha] para [coluna])
#           Sol Nublado Chuva
transicoes = {
    'Sol':      {'Sol': 0.7, 'Nublado': 0.2, 'Chuva': 0.1},
    'Nublado':  {'Sol': 0.3, 'Nublado': 0.4, 'Chuva': 0.3},
    'Chuva':    {'Sol': 0.2, 'Nublado': 0.3, 'Chuva': 0.5}
}

print("\nMatriz de Transição (Probabilidade de ir de [linha] para [coluna]):")
for estado, prob in transicoes.items():
    print(f"De {estado}: {prob}")

# 3. Definir o estado inicial (onde estamos começando)
estadoAtual = random.choice(estados) # começa aleatoriamente
# ou podemos fixar: estadoAtual = 'Sol'
print(f"\nComeçando com o tempo: {estadoAtual}")

# 4. Simular a Sequência de Eventos
numDias = 10 # Quantos dias queremos simular
historicoTempo = [estadoAtual]

print(f"\nPrevisão do tempo para os próximos {numDias} dias:")

for dia in range(numDias):
    # Obter as probabilidades de transição do estado atual
    proximasProbabilidades = transicoes[estadoAtual]

    # Obter os possíveis próximos estados e suas probabilidades
    proximosEstados = list(proximasProbabilidades.keys())
    probabilidades = list(proximasProbabilidades.values())

    # Escolher o próximo estado com base nas probabilidades
    proximoEstado = random.choices(proximosEstados, weights=probabilidades, k=1)[0]

    historicoTempo.append(proximoEstado)
    estadoAtual = proximoEstado # Atualiza o estado para a próxima iteração

print(f"Sequência de tempo simulada: {historicoTempo}")

print("\n--- Analisando Frequências na simulação ---")
from collections import Counter
frequenciasSimuladas = Counter(historicoTempo)
print(f"Frequência de ocorrência dos estados na simulação: {frequenciasSimuladas}")