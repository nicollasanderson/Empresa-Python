# Desenvolva a classe de Empresa aqui
import ujson as json
import os
from datetime import datetime

class Empresa:
    def __init__(self,nome: str,cnpj: str):
        self.nome = ' '.join(nome.split()).title()
        self.cnpj = cnpj
        self.contratados = []

    def contratar_funcionario(self, funcionario: object):
        user_name = funcionario.nome_completo.replace(' ', "_").lower()
        company_name = self.nome.replace(' ', "_").lower()

        funcionario.email = f"{user_name}@{company_name}.com"
        funcionario.empresa = self.nome

        for value in self.contratados:
            if funcionario.cpf == value["cpf"]:
                return "Funcionário com esse CPF já foi contratado."

        self.contratados.append(funcionario.__dict__)
        return "Funcionário contratado!"

    def gerar_holerite(self, funcionario):
        user_exist = self.contratados.count(funcionario.__dict__)
        
        if user_exist == 0:
            return False

        company_name = self.nome.replace(' ', "_").lower()
        user_name = funcionario.nome_completo.replace(' ', "_").lower()
        data = funcionario.__dict__
        data["mes"] = datetime.now().strftime("%B")
        data.pop('empresa')
        data.pop('email')

        try:
            dir = os.path.abspath(f"./empresas")
            new_dir = os.path.join(dir, company_name, user_name)
            
            os.makedirs(new_dir)

            with open(f"{new_dir}/{user_name}.json", "w") as write_file:
                json.dump(data, write_file, indent=2)
        except:
            return "Pasta já criada"

        return True
        
    def __len__(self):
        return len(self.contratados)