'''def soma():
    print("Imprimindo função na tela")

soma()'''

'''def soma():
    txt = "Imprimindo resultado com variável"
    return txt

print(soma())'''

def soma(a,b,c):
    d = a + b + c
    return d

print(soma(6,9,2))

'''def verif_par(a,b,c):
    d = a + b + c
    if d % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
print(verif_par(3,5,2))'''

def verif_par(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
print(verif_par(35))
print(verif_par(soma(5,9,2)))