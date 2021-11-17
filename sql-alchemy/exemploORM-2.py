# INSTALAR O MÓDULO SQLALCHEMY
# Executar no terminal o comando: pip install sqlalchemy

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float, desc
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

# SCRIPT PARA CRIAR UMA NOVA TABELA NO BANCO DE DADOS
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INT,
                        SALARIO FLOAT)
                    """)

# DEFINIÇÃO DE CLASSE QUE MAPEIA UMA TABELA


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):   # Método construtor da classe
        self.nome = nome
        self.idade = idade
        self.salario = salario


# -----------------------------------------------------------------------------
# INSERINDO DADOS NA TABELA

# Inserir um objeto
func = Funcionario('Zezinho', 20, 1700)
session.add(func)                       # insere os dados de um objeto
session.commit()                        # necessario fazer o commit()

# Inserir uma lista de objetos
func1 = Funcionario('Luizinho', 22, 1250)
func2 = Funcionario('Huguinho', 22, 2200)
lista = [func1, func2]
session.add_all(lista)                  # insere os dados de todos os objetos
session.commit()

# Inserir objetos cadastrados pelo usuário
'''
for _ in range(3):
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    salario = float(input('Informe o salrio: '))
    func = Funcionario(nome, idade, salario)
    session.add(func)
    session.commit()
'''

lista = []
while True:
    nome = input('Informe o nome (Digite SAIR para finalizar): ')
    if nome == 'SAIR':
        break
    idade = int(input('Informe a idade: '))
    salario = float(input('Informe o salario: '))
    func = Funcionario(nome, idade, salario)
    lista.append(func)
session.add_all(lista)
session.commit()

# -----------------------------------------------------------------------------
# CONSULTANDO OS DADOS DA TABELA

# Consultar todos os dados
print('-'*30)
resultado = session.query(Funcionario).order_by(desc(Funcionario.nome))
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

# Consultar utilizando filtros (salario maior que 1500)
print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500, Funcionario.idade == 22)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.nome.like('%inho%'))
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)

# Consultar pela chave primária
print('-'*30)
func = session.query(Funcionario).get(5)
if func is not None:
    print(func.id, func.nome, func.idade, func.salario)
else:
    print('ID inexistente')

# exemplo de top 1
print('-'*30)
resultado = session.query(Funcionario).order_by(Funcionario.nome).limit(1)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)


# exemplo de count
n = session.query(Funcionario).filter(Funcionario.salario <= 1500).count()
print(n)

# -----------------------------------------------------------------------------
# ALTERANDO DADOS
func = session.query(Funcionario).get(6)
if func is not None:
    func.salario = 3500
    func.nome = 'João da Silva'
    session.commit()
else:
    print("ID inexistente")


# aumenta em 10% o salario de todos os funcionarios
lista = session.query(Funcionario)
for func in lista:
    func.salario += func.salario * 0.10
session.commit()

# -----------------------------------------------------------------------------
# EXCLUINDO DADOS

# Excluir um objeto
func = session.query(Funcionario).get(2)        # busca um funcionário pelo id
if func is not None:
    session.delete(func)
    session.commit()

# ----------------------------------------------------------------------------
# CONSULTA TODOS OS DADOS
print('-'*30)
resultado = session.query(Funcionario)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)
