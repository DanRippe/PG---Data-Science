# Desafio 1:
# Fazer o sistema de verificação de maioridade usando funções

def verif_maioridade(ano,mes,dia):
    from datetime import date
    hoje = date.today()
    nascimento = date(ano,mes,dia)
    idade = hoje - nascimento
    anos  = idade.days / 365
    
    if anos >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verif_maioridade(1989,4,21))
print(verif_maioridade(2010,10,9))