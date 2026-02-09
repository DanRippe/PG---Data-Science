Algoritmo "Condicional Composta"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 09/02/2026
Var
// Seção de Declarações das variáveis 
   num: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreval("Digite um número: ")
   Leia(num)
   
   se (num > 0.0) entao
      Escreval("Este número é POSITIVO")
   senao
      se (num < 0.0) entao
         Escreval("Este número é NEGATIVO")
      senao
         Escreva("Este número é NULO")
         fimse
      fimse

Fimalgoritmo