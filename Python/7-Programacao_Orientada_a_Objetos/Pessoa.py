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