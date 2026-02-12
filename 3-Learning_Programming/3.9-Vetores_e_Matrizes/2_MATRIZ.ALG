Algoritmo "Matriz"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
// Seção de Declarações das variáveis 
   numeros: vetor[1..3, 1..2] de inteiro
   i, k: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   para i de 1 ate 3 faca
       para k de 1 ate 2 faca
           escreva("Digite o valor para a linha ", i, " e coluna ", k, ": ")
           leia(numeros[i,k])
       fimpara
   fimpara
   
   para i de 1 ate 3 faca
       para k de 1 ate 2 faca
           escreva(numeros[i,k], ", ")
       fimpara
       escreval("")
   fimpara
   
Fimalgoritmo