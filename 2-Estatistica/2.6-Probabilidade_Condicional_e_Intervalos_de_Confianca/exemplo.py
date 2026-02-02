import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo: Notas dos Alunos (dados quantitativos discretos)
notas = [7, 8, 6, 7, 9, 5, 7, 8, 6, 7, 5, 7, 8, 9, 6, 7, 8, 6, 7, 8]

print("\n1. Distribuição de Frequências")

# Criando uma Series Pandas para facilitar o cálculo das frequências
seriesNotas = pd.Series(notas)

# Frequência Absoluta: Contagem de cada nota
freqAbsoluta = seriesNotas.value_counts().sort_index()
print("\nFrequência Absoluta:\n", freqAbsoluta)

# Frequência Relativa: Proporção de cada nota
freqRelativa = seriesNotas.value_counts(normalize=True).sort_index()
print("\nFrequência Relativa:\n", freqRelativa)

# Frequência Acumulada Absoluta: Soma progressiva das frequências absolutas
freqAcumuladaAbsoluta = freqAbsoluta.cumsum()
print("\nFrequência Acumulada Absoluta:\n", freqAcumuladaAbsoluta)

# Frequência Acumulada Relativa: Soma progressiva das frequências relativas
freqAcumuladaRelativa = freqRelativa.cumsum()
print("\nFrequência Acumulada Relativa:\n", freqAcumuladaRelativa)

# Criando um DataFrame para a tabela de frequências completa e formatada
df_Frequencias = pd.DataFrame({
    'Frequência Absoluta (f)': freqAbsoluta,
    'Frequência Relativa (fr)': freqRelativa.map('{:.2%}'.format),
    'Frequência Absoluta Acumulada (F)': freqAcumuladaAbsoluta,
    'Frequência Acumulada Relativa (Fr)': freqAcumuladaRelativa.map('{:.2%}'.format)
})
print("\nTabela de Frequências Completa:\n", df_Frequencias)

print("\n2. Representação Gráfica")

# Gráfico de barras (para Notas - dados quantitativos discretos, tratados como categorias neste caso)
plt.figure(figsize=(8,5))
freqAbsoluta.plot(kind='bar', color='skyblue')
plt.title('Frequência das Notas dos Alunos')
plt.xlabel('Nota')
plt.ylabel('Frequência Absoluta')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Setores (Pizza) - para dados categóricos/discretos com poucas opções
plt.figure(figsize=(8,8))
freqAbsoluta.plot(kind='pie', autopct='%1.1%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribuição Percentual das Notas')
plt.ylabel('')
plt.show()

# Histograma (para dados quantitativos contínuos)
# Gerando dados de exemplos para alturas, que são contínuos
np.random.seed(42) # para dados reprodutíveis
dadosAltura = np.random.normal(170, 10, 1000) # Média 170cm, desvio padrão 10cm, 1000 observações

plt.figure(figsize=(10,6))
plt.hist(dadosAltura, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
plt.title('Histograma de Alturas(cm)')
plt.xlabel('Altura(cm)')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de linhas (para dados ao longo do tempo ou ordem)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [150, 180, 220, 190, 250, 230]

plt.figure(figsize=(9,5))
plt.plot(meses, vendas, marker='o', linestyle='-', color='purple')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()