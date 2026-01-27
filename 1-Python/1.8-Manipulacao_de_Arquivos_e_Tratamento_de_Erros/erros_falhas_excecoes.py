# uma falha é caracterizada por um comportamento inesperado no código
# Exemplo: queremos que o resultado da soma de dois números seja multiplicado por outro número

'''
a = 4 + 6 * 5
'''
# O resultado esperado é 50, mas nesse caso será 34, pois é respeitada a regra de que a multiplicação é resolvida primeiro

'''
a = (4 + 6) * 5
'''
# Essa é a forma correta de fazer o cálculo proposto, a operação entre parênteses é resolvida primeira

#############################################################################################################################

# um erro é caracterizado, essencialmente, por um erro na sintaxe do código, e retornará uma mensagem explicitando esse erro
# Exemplo: fazer uma soma da seguinte maneira:

'''
a = 5 + "9"
'''
# retorna um erro, pois não é possível somar um inteiro com uma string
# é comum que isso acontece quando o valor é proveniente de um "input", pois sem ser convertido, sempre retorna uma string

#############################################################################################################################

# uma exceção não é nem uma falha, nem um erro
# normalmente ocorre quando o código funciona perfeitamente em um cenário, e em outro não
# Exemplo:

''' b = 12
    c = 4

    a = b / c'''
# não há erro nessa linha e ela executa normalmente

# mas se fizermos a seguinte alteração:
''' b = 12
    c = 0

    a = b / c'''
# não há erro de sintaxe, mas nenhum número pode ser dividido por 0, retornando um "erro por exceção"
# é comum que isso ocorra quando os valores são inseridos pelo usuário através de um "input" que não previna esse tipo de condição

#Exemplo:
'''
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if b == 0:
    print("Não é possível dividir um número por zero.")
else:
    resultado = a / b
    print(resultado)
'''

#ou:

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

while b == 0:
    b = int(input("Um número não pode ser dividido por zero, digite outro: "))

resultado = a / b
print(resultado)