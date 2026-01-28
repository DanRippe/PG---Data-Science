import random
import pandas as pd
import numpy as np

print("--- Método Estatístico: Da Coleta à Análise ---")

# 1. Coleta de Dados (Simulada)
# Vamos simular uma população de "alunos" com seus cursos e notas
populacaoAlunos = pd.DataFrame({
    'ID': range(1, 101),
    'Curso': ['Engenharia'] * 30 + ['Medicina'] * 40 + ['Direito '] * 30,
    'Nota Final': np.random.randint(50, 101, 100)
})

print("1. Coleta de Dados: Nossa População Simulada (primeiras 5 linhas)")
print(populacaoAlunos.head())
print(f"\nTamanho total da população: {len(populacaoAlunos)} alunos")
print(f"Distribuição de cursos na população:\n{populacaoAlunos['Curso'].value_counts()}")

# 2. Organização e Apresentação dos Dados
print("\n2. Organização e Apresentação de Dados:")
print("\nDescrição Estatística básica da nota final na população:")
print(populacaoAlunos['Nota Final'].describe())

# 3. Análise de Dados (Estatística Descritiva e Amostragem)
print("\n3. Técnicas de Amostragem")

# 3.1 Amostragem Aleatória Simples (AAS)
# Cada aluno tem a mesma chance de ser selecionado
tamanhoAmostraAAS = 20
amostraAAS = populacaoAlunos.sample(n=tamanhoAmostraAAS, random_state=None)

print(f"\n3.1 AAS - Amostra Aleatória Simples (n={tamanhoAmostraAAS}):")
print(amostraAAS.head())
print(f"Média da nota final na amostra AAS: {amostraAAS['Nota Final'].mean():.2f}")
print(f"Distribuição de cursos na amostra AAS:\n{amostraAAS['Curso'].value_counts()}")
print("A distribuição de cursos pode não ser proporcional à população na AAS")

# 3.2 Amostragem Estratificada
# Garante que cada "estrato" (grupo, no caso, curso) seja proporcionalmente representado

amostraEstratificada = populacaoAlunos.groupby('Curso').apply(
    lambda x: x.sample(frac=tamanhoAmostraAAS / len(populacaoAlunos), random_state=None)
).reset_index(drop=True)

print(f"\n3.2 Amostra Estratificada (n={len(amostraEstratificada)}):")
print(amostraEstratificada.head())
print(f"Média da nota final na amostra estratificada: {amostraEstratificada['Nota Final'].mean():.2f}")
print(f"Distribuição de cursos na amostra estratificada:\n{amostraEstratificada['Curso'].value_counts()}")
print("Observe que a distribuição de cursos da amostra estratificada é bem próxima à da população")

# 4. Interpretação dos Resultados
print("\n4. Interpretação dos Resultados")
print(f"Média da nota final da população inteira: {populacaoAlunos['Nota Final'].mean():.2f}")
print(f"Média da nota final na amostra AAS: {amostraAAS['Nota Final'].mean():.2f}")
print(f"Média da nota final na amostra estratificada: {amostraEstratificada['Nota Final'].mean():.2f}")

print("\nObservação:")
print("- A média da amostra(estatística) é uma estimativa da média da população(parâmetro)")
print("- A amostra estratificada geralmente fornece uma estimativa mais precisa se houver")
print("  grupos importantes na população que você quer garantir que sejam representados")
print("- A AAS é mais simples, mas pode não capturar bem a diversidade em amostras pequenas")