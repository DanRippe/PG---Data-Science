class Aluno:
    
    def __init__(self, nome, cpf, email, matricula, nota1, nota2, nota3, nota4):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._matricula = matricula
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
        self._nota4 = nota4

        @property
        def nome(self):
            return self._nome
        
        @nome.setter
        def nome(self, nome):
            self._nome = nome

        @property
        def cpf(self):
            return self._cpf
        
        @cpf.setter
        def cpf(self, cpf):
            self._cpf = cpf

        @property
        def email(self):
            return self._email
        
        @email.setter
        def email(self, email):
            self._email = email

        @property
        def matricula(self):
            return self._matricula
        
        @matricula.setter
        def matricula(self, matricula):
            self._matricula = matricula

        @property
        def nota1(self):
            return self._nota1
        
        @nota1.setter
        def nota1(self, nota1):
            self._nota1 = nota1

        @property
        def nota2(self):
            return self._nota2
        
        @nota2.setter
        def nota2(self, nota2):
            self._nota2 = nota2

        @property
        def nota3(self):
            return self._nota3
        
        @nota3.setter
        def nota3(self, nota3):
            self._nota3 = nota3

        @property
        def nota4(self):
            return self._nota4
        
        @nota4.setter
        def nota4(self, nota4):
            self._nota4 = nota4