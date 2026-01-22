# Desafio 2:
# Fazer uma contagem de 0 a 10 usando recursão
# Fazer a mesma contagem, mas regressiva, de 10 a 0

# contagem progressiva
def contagem_p(nIp,nFp):
    if nIp == nFp:
        print(nFp)
    else:
        print(nIp)
        contagem_p(nIp+1,nFp)
    
#contagem_p(0,10)

#contagem regressiva
def contagem_r(nIr,nFr):
    if nIr == nFr:
        print(nFr)
    else:
        print(nIr)
        contagem_r(nIr-1,nFr)
    
#contagem_r(10,0)

def contagem(nI,nF):
    if nI == nF:
        print(nI)
    elif nI < nF:
        contagem_p(nI,nF)
    else:
        contagem_r(nI,nF)

contagem(5,10)
contagem(100,88)