# Desenvolva a classe de Gerente aqui
from classes.funcionario import Funcionario

class Gerente(Funcionario):

    funcao = "Gerente"

    def __init__(self, nome_completo,cpf,salario = 8000):

        Funcionario.__init__(self,nome_completo,cpf)
        self.salario = salario
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        for value in self.funcionarios:
            if value.cpf == funcionario.cpf:
                return False
                
        if funcionario.funcao != "Gerente" and funcionario.empresa == self.empresa:
            self.funcionarios.append(funcionario)
            return True

        return False

    def __len__(self):
        return len(self.funcionarios)