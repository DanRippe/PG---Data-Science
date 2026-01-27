import collections
import numpy as np
import matplotlib.pyplot as plt

########## Tipos de Dados Estatísticos ##########

##### 1. Dados Qualitativos (Categóricos) #####

# 1.1. Qualitativos nominais #
coresFavoritas = ["Azul", "Verde", "Vermelho", "Azul", "Amarelo", "Verde", "Azul", "Vermelho"]
print("1.1. Dados Qualitativos Nominais (Ex: Cores Favoritas)")
print(f"Dados: {coresFavoritas}")

# Estatística Descritiva para Dados Nominais: Contagem de Frequência (Moda)
frequenciaCores = collections.Counter(coresFavoritas)
print(f"Frequência das Cores: {frequenciaCores}")
print(f"Moda (Cor mais comum): {frequenciaCores.most_common(1)[0][0]}")

# 1.2. Qualitativos Ordinais #
niveisSatisfacao = ["Bom", "Ruim", "Excelente", "Bom", "Regular", "Excelente", "Ruim"]
print("\n1.2. Dados Qualitativos Ordinais (Ex: Níveis de Satisfação)")
print(f"Dados: {niveisSatisfacao}")

# Para ordinais, podemos ordenar para ver a distribuição, mas a média não faz sentido
# A moda ainda é útil
frequenciaSatisfacao = collections.Counter(niveisSatisfacao)
print(f"Frequência dos níveis: {frequenciaSatisfacao}")
print(f"Moda: {frequenciaSatisfacao.most_common(1)[0][0]}")

##### 2. Dados Quantitativos (Numéricos) #####

# 2.1. Quantitativos Discretos #
numeroFilhos = [0, 1, 2, 1, 3, 0, 1, 2, 1, 0, 2]
print("\n2.1. Dados Quantitativos Discretos (Ex: Número de Filhos)")
print(f"Dados: {numeroFilhos}")

# 2.2. Quantitativos Contínuos #
alturas_cm = [175.5, 168.2, 180.0, 172.1, 165.9, 178.5, 170.0, 181.3]
print("\nDados Quantitativos Contínuos (Ex: Alturas em cm)")
print(f"Dados: {alturas_cm}")

print("\n--- Tipos de Estatística: Estatística Descritiva em ação")
# A Estatística Descritiva resume e organiza dados

# usando dados quantitativos (alturas) para demonstrar medidas descritivas
dadosParaAnalise = np.array(alturas_cm)

# Medidas de tendência central (onde os dados se concentram)
media = np.mean(dadosParaAnalise)
mediana = np.median(dadosParaAnalise)

# A moda para dados contínuos pode ser complexa, mas para dados discertos é mais simples
# para este exemplo, vamos simplificar a moda para o valor mais frequente
from scipy import stats
try:
    moda = stats.mode(dadosParaAnalise)[0][0]  # pega o primeiro valor da moda, se houver
except IndexError:                             # caso não haja moda única
    moda = "Não aplicável ou múltiplos valores"

print("\nEstatística Descritiva para Alturas:")
print(f"Média: {media:.2f} cm")
print(f"Mediana: {mediana:.2f} cm")
print(f"Moda: {moda}")                         # a moda pode ser menos relevante para dados contínuos

# Medidas de dispersão (quão espalhados estão os dados)
desvioPadrao = np.std(dadosParaAnalise)
amplitude = np.max(dadosParaAnalise) - np.min(dadosParaAnalise)

print(f"Desvio Padrão: {desvioPadrao:.2f} cm")
print(f"Amplitude: {amplitude:.2f} cm")

# Visualização de dados (Histograma) - Uma ferramenta descritiva
plt.figure(figsize=(8, 5))
plt.hist(dadosParaAnalise, bins=4, edgecolor='black', alpha=0.7, color='purple')
plt.title('Histograma das Alturas (cm)')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Média: {media:.2f}')
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()