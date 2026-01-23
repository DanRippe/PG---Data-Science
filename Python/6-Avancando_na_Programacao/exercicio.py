'''Desafio:
Criar uma função, preferencialmente recursiva, para verificar
se o valor "Descomplica" está presente entre um dos nomes inseridos na lista
se foi: exibir apenas o nome "Descomplica"
senão: exibir todos os nomes'''

listaNomes = []

for a in range(5):
    listaNomes.append(input("Nome: "))

'''print(listaNomes)
a = set(listaNomes)
b = []
b.append("Descomplica")
c = set(b)
print(a)
print(c)

print(a.intersection(b))'''

def verif_item_na_lista(item,lista):
    a = set(lista)
    c = []
    c.append(item)
    b = set(c)

    if set(a.intersection(b)) == b:
        print(b)
    else:
        print(a)

verif_item_na_lista("Descomplica",listaNomes)