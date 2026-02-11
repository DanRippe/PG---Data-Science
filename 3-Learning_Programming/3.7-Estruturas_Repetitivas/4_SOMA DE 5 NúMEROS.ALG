Algoritmo "Soma de 5 Números"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis 
   i, num, soma: inteiro
   j, num2, mult: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   i <- 1
   enquanto i <= 5 faca
            escreval("Digite um número: ")
            leia(num)
            soma <- soma + num
            i <- i + 1
   fimenquanto
   
   escreval("A soma dos números é: ", soma)
   
   mult <- 1
   para i de 1 ate 4 faca
        escreval("Digite um número: ")
        leia(num2)
        mult <- mult * num2
   fimpara
   
   escreval("A multiplicação dos números é: ", mult)

Fimalgoritmo