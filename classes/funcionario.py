# Desenvolva a classe de Funcionario aqui
from datetime import datetime

class Funcionario():
    
    funcao = "Funcionário"

    def __init__(self,nome_completo, cpf, salario = 3000):
        self.nome_completo = ' '.join(nome_completo.split()).title()
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime('%d/%m/%Y')

    def __str__(self):
        return f"{self.nome_completo[0]} - {self.funcao}"