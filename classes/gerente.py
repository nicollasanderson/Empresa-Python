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
            self.funcionarios.append(funcionario.__dict__)
            return True

        return False

    def aumento_salarial(self, funcionario, empresa):
        for value in empresa.contratados:
            if "funcionarios" in value:
                for func in value['funcionarios']:
                    if func['cpf'] == funcionario.cpf:
                        novo_salario = (funcionario.salario * 0.1) + funcionario.salario

                        if int(novo_salario) >= 8000:
                            result = empresa.promocao(funcionario)
                            result.salario = int(novo_salario)
                            return result

                        funcionario.salario = int(novo_salario)
                        return funcionario

        return False

    def __len__(self):
        return len(self.funcionarios)