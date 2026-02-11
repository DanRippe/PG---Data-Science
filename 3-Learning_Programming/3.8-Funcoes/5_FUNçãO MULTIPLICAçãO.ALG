Algoritmo "Função Multiplicação"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
   funcao produto(x,y: real): real
   var
       total: real

   inicio
       total <- x * y
       retorne total
   fimfuncao
Var
// Seção de Declarações das variáveis 
   valor1, valor2, res: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva("Digite o primeiro número: ")
   leia(valor1)
   escreva("Digite o segundo número: ")
   leia(valor2)
   
   res <- produto(valor1, valor2)
   
   escreva("O produto dos números é: ", res)

Fimalgoritmo