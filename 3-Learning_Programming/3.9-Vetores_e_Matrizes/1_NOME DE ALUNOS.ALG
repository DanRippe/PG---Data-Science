Algoritmo "Nome de Alunos"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
// Seção de Declarações das variáveis 
   nomesAlunos: vetor[1..5] de caractere
   contador: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   para contador de 1 ate 5 faca
       escreva("Digite o nome do(a) aluno(a) número ", contador, " de 5:")
       leia(nomesAlunos[contador])
   fimpara

   contador <- 1
   
   para contador de 1 ate 5 faca
       escreval("Nome do(a) Aluno(a) ", contador, ": ", nomesAlunos[contador])
   fimpara
   
Fimalgoritmo