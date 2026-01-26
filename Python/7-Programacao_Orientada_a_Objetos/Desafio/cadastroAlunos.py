from Aluno import Aluno

listaAlunos = []
pergunta = "s"

while pergunta == "s":
    aluno = Aluno(0,0,0,0,0,0,0,0)
    aluno.nome = (input("\nDigite o nome do(a) aluno(a): "))
    aluno.cpf = (input("Insira o CPF: "))
    aluno.email = (input("Agora o e-mail: "))
    aluno.matricula = (input("Por fim, a matrícula: "))
    aluno.nota1 = (int(input("Insira a primeira nota: ")))
    aluno.nota2 = (int(input("A segunda: ")))
    aluno.nota3 = (int(input("E a terceira: ")))
    listaAlunos.append(aluno)

    pergunta = input("\nDeseja cadastar um(a) novo(a) aluno(a? (s/n) ")

for alunos in listaAlunos:
    media = (alunos.nota1 + alunos.nota2 + alunos.nota3) / 3

    if media >= 6:        
        print(f'\nAluno(a) {alunos.nome} foi aprovado(a). Seu diploma terá os seguintes dados:')
        print(f'Nome: {alunos.nome}')
        print(f'CPF: {alunos.cpf}')
        print(f'E-mail: {alunos.email}')
        print(f'Matrícula: {alunos.matricula}')
        print(f'Notas: {alunos.nota1}, {alunos.nota2}, {alunos.nota3}')

    else:        
        alunos.nota4 = (int(input(f'\nAluno(a) {alunos.nome} ainda não foi aprovado(a), insira a nota da recuperação: ')))        
        media = (alunos.nota1 + alunos.nota2 + alunos.nota3 + alunos.nota4) / 4

        if media >= 6:
            print(f'Aluno(a) {alunos.nome} agora foi aprovado(a). Seu diploma terá os seguintes dados:')
            print(f'Nome: {alunos.nome}')
            print(f'CPF: {alunos.cpf}')
            print(f'E-mail: {alunos.email}')
            print(f'Matrícula: {alunos.matricula}')
            print(f'Notas: {alunos.nota1}, {alunos.nota2}, {alunos.nota3}, {alunos.nota4}')
        
        else:
            print(f'É uma pena, mas o(a) aluno(a) {alunos.nome} foi reprovado(a).')