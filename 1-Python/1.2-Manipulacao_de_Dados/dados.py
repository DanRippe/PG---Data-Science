nome = input("Digite seu nome: ")
nascimento = input("Qual seu ano de nascimento? ")
email = input("Digite seu e-mail: ")

print("Nome:", nome, ". E-mail:", email, ". Nascimento: ", nascimento, ".")
# a virgula concatena informacoes no output "print"

a = int(input("Digite um numero: "))
# a funcao input() so trabalha com string, caso um numero seja digitado, tambem sera tratado como tal
# a funcao int() está convertendo a string recebida no input em um valor numerico inteiro

print(a + 5)
# o print está mostrando o resultado da soma da entrada, convertida em numero, com o valor 5

b = float(input("Digite um valor com casa decimal: "))
# a funcao float() converte para um numero real, do tipo double/float

print(b + 10)