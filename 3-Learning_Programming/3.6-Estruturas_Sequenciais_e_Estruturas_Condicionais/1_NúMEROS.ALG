Algoritmo "Números"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 09/02/2026
Var
// Seção de Declarações das variáveis 
   num1: inteiro
   num2: inteiro
   soma: inteiro
   media: real
   produto: real
   exponenciacao: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Esse programa calculará a soma, a média, o produto ")
   Escreval("e a exponenciação entre dois números.")
   Escreval("Digite o primeiro número: ")
   Leia(num1)
   Escreval("Agora digite o segundo número: ")
   Leia(num2)
   
   soma <- num1 + num2
   media <- soma / 2
   produto <- num1 * num2
   exponenciacao <- num1 ^ num2
   
   Escreval("A soma entre os números é: ", soma)
   Escreval("A média é: ", media)
   Escreval("O produto é: ", produto)
   Escreval("E a exponenciação é: ", exponenciacao)

Fimalgoritmo