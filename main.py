from classes.funcionario import Funcionario
from classes.empresa import Empresa

if __name__ == "__main__":
    pass
    empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
    print(empresa_1.__dict__)

    print(len(empresa_1))

    funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
    funcionario_2 = Funcionario("  stephen  alves curry ", "12332145665")

    # CPF CORRETO
    resposta = empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(funcionario_2)
    print(resposta) 
    # Funcionário contratado!
    print(f'CONTRATADOS: {len(empresa_1)}')
    # CONTRATADOS: 2
    print(f'EMAIL: {funcionario_1.email}')
    # Email: jordan_cardoso_poole@kenziebrasil.com
    print(f'Empresa: {funcionario_1.empresa}')
    # Empresa: Kenzie Brasil

    # CPF REPETIDO
    resposta = empresa_1.contratar_funcionario(funcionario_2)
    print(resposta) 
    # Funcionário com esse CPF já foi contratado.
    holerite = empresa_1.gerar_holerite(funcionario_1)
    print(holerite)
    # True

    # Funcionario não contratado
    funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
    holerite = empresa_1.gerar_holerite(funcionario_3)
    print(holerite)
    # False