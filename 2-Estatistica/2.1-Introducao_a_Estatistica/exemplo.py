import random

##### 1. Definindo a População #####
populacaoNotas = [6.5, 7.0, 8.0, 5.5, 9.0, 7.5, 6.0, 8.5, 7.0, 9.5, 6.0, 5.0, 7.0, 8.0, 9.0]

print("--- Nossa População ---")
print(f"População de Notas: {populacaoNotas}")
print(f"Tamanho da População: {len(populacaoNotas)}")

# Calculando a média da população (um parâmetro)
mediaPopulacao = sum(populacaoNotas) / len(populacaoNotas)
print(f"Média da População (Parâmetro): {mediaPopulacao:.2f}")

##### 2. Tirando uma amostra #####
tamanhoAmostra = 5
amostraNotas = random.sample(populacaoNotas, tamanhoAmostra)

print("\n--- Nossa Amostra ---")
print(f"Amostra de Notas: {amostraNotas}")
print(f"Tamanho da Amostra: {len(amostraNotas)}")

# Calculando a média da amostra (uma estatística)
mediaAmostra = sum(amostraNotas) / len(amostraNotas)
print(f"Média da Amostra (Estatística): {mediaAmostra:.2f}")

##### 3. Comparando População e Amostra #####
print("\n--- Comparação ---")
print(f"Média da População (Parâmetro): {mediaPopulacao:.2f}")
print(f"Média da Amostra (Estatística): {mediaAmostra:.2f}")
print(f"Diferença entre as médias: {(mediaAmostra - mediaPopulacao):.2f}")

print("\nA média da amostra é uma estimativa da média da população, mas geralmente não é idêntica a ela.")
print("Quanto maior a amostra (e se for bem selecionada), mais próxima tende a ser da população.")