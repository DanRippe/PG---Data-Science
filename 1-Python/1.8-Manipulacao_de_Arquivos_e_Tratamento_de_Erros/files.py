# R = Read
# W = Write
# X = eXecute
# A = Append
# R+
# WB

'''Manipular arquivos locais'''

#open("teste.txt", "x")

#conteudo = open("arquivo.txt", "a")
#conteudo.write("\nAdicionando uma linha")
#conteudo.write("\nAdicionando outra linha")
#conteudo.close()

#conteudo = open("arquivo.txt", "r")
#print(conteudo.read())

'''Manipular arquivos da internet'''

import requests

lerArquivo = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")
#print(lerArquivo.text)
''' na aula é utilizado somente "print(lerArquivo)", mas aqui só retorna o código 200 e nenhum conteúdo'''

with open("arquivoInternet.txt", "wb") as arquivo:
    arquivo.write(lerArquivo.content)