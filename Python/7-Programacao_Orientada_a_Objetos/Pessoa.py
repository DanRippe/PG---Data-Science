# Por convenção, a declaração de uma classe se inicia com a letra maiúscula.
# Atributos = Variáveis
# Método = Função

class Pessoa:
    #atributos
    nome = "Danilo"
    idade = 36

    #método
    def exibir(self):       #self indica que será utilizado um valor de dentro da própria classe e não um valor externo
        print(self.nome)
        print(self.idade)

    #método construtor
    #def __init__(self, nome, idade):
    #    self.nome = nome
    #    self.idade = idade
    #    print(self.nome)
    #    print(self.idade)

    #GETTERS E SETTERS
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome