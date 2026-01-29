import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo: Notas dos alunos
notas = [7, 8, 6, 7, 9, 5, 7, 8, 6, 7, 5, 7, 8, 9, 6, 7, 8, 6, 7, 8]

# 1. Distribuição de frequências
# Crindo uma "series" com "pandas" para facilitar o cálculo de frequências
seriesNotas = pd.Series(notas)

# Frequência Absoluta
frequenciaAbsoluta = seriesNotas.value_counts().sort_index()
print("Frequência Absoluta:\n", frequenciaAbsoluta)

# Frequência Relativa
frequenciaRelativa = seriesNotas.value_counts(normalize=True).sort_index()
print("\nFrequência Relativa:\n", frequenciaRelativa)

#Frequência Acumulada Absoluta
frequenciaAcumuladaAbsoluta = frequenciaAbsoluta.cumsum()
print("\nFrequência Acumulada Absoluta:\n", frequenciaAcumuladaAbsoluta)

#Frequência Acumulada Relativa
frequenciaAcumuladaRelativa = frequenciaRelativa.cumsum()
print("\nFrequência Acumulada Relativa:\n", frequenciaAcumuladaRelativa)

# Criando um DataFrame para a tabela de frequências completa
df_Frequencias = pd.DataFrame({
    'Frequência Absoluta (f)': frequenciaAbsoluta,
    'Frequência Relativa (fr)': frequenciaRelativa.map('{:.2%}'.format), # formatado como porcentagem
    'Frequência Acumulada (F)': frequenciaAcumuladaAbsoluta,
    'Frequência Acumulada Relativa (Fr)': frequenciaAcumuladaRelativa.map('{:.2%}'.format)
})

print("\nTabela de Frequências Completa:\n", df_Frequencias)

# 2. Representação Gráfica

# Gráfico de Barras (para notas)
plt.figure(figsize=(8,5))
frequenciaAbsoluta.plot(kind='bar', color='skyblue')
plt.title('Frequência de Notas dos Alunos')
plt.xlabel('Nota')
plt.ylabel('Frequência Absoluta')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Setores (Pizza)
plt.figure(figsize=(8,8))
frequenciaAbsoluta.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribuição Percentual das Notas')
plt.ylabel('')
plt.show()

# Histograma (para dados contínuos ou para muitas categorias)
# Vamos gerar dados de exemplo que se assemelham a uma distribuição contínua
np.random.seed(42)
dadosAltura = np.random.normal(170, 10, 1000) # média 170cm, desvio padrão 10cm, 1000 observações

plt.figure(figsize=(10,6))
plt.hist(dadosAltura, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
plt.title('Histograma de Alturas (cm)')
plt.xlabel('Altura (cm)')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Linhas (para dados ao longo do tempo ou ordem)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [150, 180, 220, 190, 250, 230]

plt.figure(figsize=(9,5))
plt.plot(meses, vendas, marker='o', linestyle='-', color='purple')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()