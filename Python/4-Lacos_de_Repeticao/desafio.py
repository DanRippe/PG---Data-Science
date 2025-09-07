# Desenvolver Algoritmo:
# - Diretor cadastra alunos com os dados:
# -- Nome, CPF, e-mail, Matrícula
# Para cada aluno cadastrado, o diretor pode lançar 3 notas
# Se a média atingida for maior ou igual a 6, escrever:
#   - Aluno X, você foi aprovado. Seu diploma terá os seguintes dados:
# *Listar todos os dados do referido aluno
# Caso a média seja inferior a 6, lançar uma nova nota e tirar nova média
# Senaõ, aluno reprovado

alunos = []
pergunta = "s"

while pergunta == "s":
    lista = []
    lista.append(input("Digite o nome do aluno: "))
    lista.append(input("Insira o CPF: "))
    lista.append(input("Agora o e-mail: "))
    lista.append(input("Por fim, a matrícula: "))
    lista.append(int(input("Insira a primeira nota: ")))
    lista.append(int(input("A segunda: ")))
    lista.append(int(input("E a terceira: ")))
    alunos.append(lista)
    pergunta = input("Deseja cadastar um novo aluno? (s/n) ")

for alunos in alunos:
    #print(alunos)
    notas = alunos[4:]
    media = sum(notas) / len(notas)
    #print(media)

    if media >= 6:
        print(f'Aluno {alunos[0]}, você foi aprovado. Seu diploma terá os seguintes dados:')
        print(f'Nome: {alunos[0]}')
        print(f'CPF: {alunos[1]}')
        print(f'E-mail: {alunos[2]}')
        print(f'Matrícula: {alunos[3]}')
        print(f'Notas: {alunos[4:]}')
    
    else:
        alunos.append(int(input(f'Aluno {alunos[0]}, você ainda não foi aprovado, insira a nota da recuperação: ')))
        #print(alunos)
        notas = alunos[4:]
        media = sum(notas) / len(notas)

        if media >= 6:
            print(f'Aluno {alunos[0]}, agora você foi aprovado. Seu diploma terá os seguintes dados:')
            print(f'Nome: {alunos[0]}')
            print(f'CPF: {alunos[1]}')
            print(f'E-mail: {alunos[2]}')
            print(f'Matrícula: {alunos[3]}')
            print(f'Notas: {alunos[4:]}')
        
        else:
            print(f'Aluno {alunos[0]}, é uma pena, mas você foi reprovado.')


