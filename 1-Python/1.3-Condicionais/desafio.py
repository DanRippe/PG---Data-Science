anoNascimento = int(input("Digite o ano do seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento

print("Informe seu título de eleitor.") if idade >= 18 else print("Informe um documento do seu responsável.")