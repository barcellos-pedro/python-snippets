# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: nome
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float, asc
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import VARCHAR

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)


# Classe para mapeamento da tabela
class Filme(Base):

    # FAZER AQUI O MAPEAMENTO DA TABELA
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    ano = Column('ANO', Integer)
    genero = Column('GENERO', String(255))
    duracao = Column('DURACAO', Integer)
    pais = Column('PAIS', String(255))
    diretor = Column('DIRETOR', String(255))
    elenco = Column('ELENCO', String(255))
    avaliacao = Column('AVALIACAO', Float)
    votos = Column('VOTOS', Integer)

    # Método construtor
    def __init__(self, titulo, ano, genero, duracao, pais, diretor, elenco, avaliacao, votos):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):
        # Cria a tabela FILME no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255),
                              ANO INT,
                              GENERO VARCHAR(255),
                              DURACAO INT,
                              PAIS VARCHAR(255),
                              DIRETOR VARCHAR(255),
                              ELENCO VARCHAR(255),
                              AVALIACAO FLOAT,
                              VOTOS INT)""")

    def incluir(self, filme):
        '''
        Recebe um objeto da classe Filme e armazena esse
        objeto no banco de dados.
        '''
        if filme is not None:
            session.add(filme)
            session.commit()
        else:
            print("O filme não existe")

    def incluir_lista(self, filmes):
        '''
        Recebe uma lista de objetos da classe Filme e armazena esses
        objetos no banco de dados
        '''
        if len(filmes) > 0:
            session.add_all(filmes)
            session.commit()
        else:
            print("Lista de filmes vazia")
            print("Nenhum filme foi adicionado")

    def alterar_avaliacao(self, id_filme, avaliacao):
        '''
        Recebe o id de um filme e altera sua nota de avaliação de
        acordo com o valor do parametro avaliacao
        '''
        filme = session.query(Filme).get(id_filme)
        if filme is not None:
            filme.avaliacao = avaliacao
            session.commit()
        else:
            print(f"Filme com o ID {id_filme} não encontrado")

    def excluir(self, id_filme):
        '''
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados
        '''
        filme = session.query(Filme).get(id_filme)
        if filme is not None:
            session.delete(filme)
            session.commit()
        else:
            print(f"Filme com o ID {id_filme} não encontrado")

    def buscar_todos(self):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos da classe Filme com todos os filmes cadastrados,
        ordenados de forma crescente pelo titulo.
        '''
        filmes = session.query(Filme).order_by(asc(Filme.titulo))
        return filmes

    def buscar_por_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos da classe Filme de um determinado ano,
        ordenados de forma crescente pelo ano
        '''
        filmes = session.query(Filme).filter(
            Filme.ano == ano).order_by(asc(Filme.titulo))
        return filmes

    def buscar_por_genero(self, genero):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos da classe Filme de um gênero específico,
        ordenados pelo titulo de forma crescente
        '''
        filmes = session.query(Filme).filter(
            Filme.genero == genero).order_by(asc(Filme.titulo))
        return filmes

    def buscar_por_elenco(self, ator):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme que tenha um determinado ator/atriz como parte
        do elenco, ordenados pelo ano de lançamento em ordem crescente
        '''
        filmes = session.query(Filme).order_by(asc(Filme.ano))
        resultado = [filme for filme in filmes if ator in filme.elenco]
        return resultado

    def buscar_melhores_do_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos da classe Filme de um determinado ano, com nota de avaliação
        maior ou igual a 90.
        Deve retornar a lista ordenada pela avaliação em ordem crescente.
        '''
        filmes = session.query(Filme).filter(
            Filme.ano == ano, Filme.avaliacao >= 90).order_by(asc(Filme.avaliacao))
        return filmes

    def exportar_filmes(self, nome_arquivo):
        '''
        Exporta os dados contidos na tabela de filmes para um arquivo de texto
        O arquivo deve conter uma listagem dos filmes, ordenados pelos titulos
        dos filmes, contendo os dados de cada filme em uma linha, no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        filmes = session.query(Filme).order_by(asc(Filme.titulo))

        arquivo = open(nome_arquivo, "w", encoding="UTF-8")

        for filme in filmes:
            arquivo.write(
                f"{filme.titulo}; {str(filme.ano)}; {filme.genero}; {str(filme.duracao)}; {filme.pais}; {filme.diretor}; {filme.elenco}; {str(filme.avaliacao)}; {str(filme.votos)}\n")

        arquivo.close()

    def importar_filmes(self, nome_arquivo):
        '''
        Recebe como parâmetro o nome de um arquivo de texto e importa os
        dados contidos no arquivo para o banco de dados.
        Considere que o arquivo contém uma listagem de filmes no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        arquivo = open(nome_arquivo, "r", encoding="UTF-8")

        for linha in arquivo:
            filme_attrs = linha.split(";")
            filme = Filme(filme_attrs[0], filme_attrs[1], filme_attrs[2], filme_attrs[3],
                          filme_attrs[4], filme_attrs[5], filme_attrs[6], filme_attrs[7], filme_attrs[8])
            session.add(filme)

        arquivo.close()


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()

# Importa filmes do arquivo movies.txt e salva no banco de dados
banco.importar_filmes('movies.txt')

# Cria um novo Filme e insere no banco de dados
filme1 = Filme("Parasite", 2019, "Comedy, Drama, Thriller", 132, "Korea",
               "Bong Joon Ho", "Song Kang-ho, Jang Hye-jin, Choi Woo-shik", 92, 40273)
banco.incluir(filme1)

# Cria uma lista com dois novos filmes e insere no banco de dados
filme2 = Filme("Joker", 2019, 'Crime, Drama, Thriller', 122, "USA",
               "Todd Phillips", "Joaquin Phoenix, Robert De Niro, Zazie Beetz", 91, 78481)
filme3 = Filme("Avengers: Endgame", 2019, 'Drama, Thriller', 181, "USA",
               "Anthony Russo, Joe Russo", "Robert Downey Jr., Chris Evans, Mark Ruffalo", 93, 715250)
lista_filmes = [filme2, filme3]
banco.incluir_lista(lista_filmes)

# Altera a avalação do filme de id 7 para 98
banco.alterar_avaliacao(7, 98)

# Exclui o filme de id 6
banco.excluir(6)

# Busca todos os filmes
lista = banco.buscar_todos()
print("[TODOS OS FILMES]")
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.diretor, f.elenco, f.avaliacao)

# Busca todos os filmes do ano de 2019
lista = banco.buscar_por_ano(2019)
print("[FILMES DE 2019]")
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano)


# Busca todos os filmes do gênero 'Crime'
lista = banco.buscar_por_genero('Crime')
print("[FILMES DE CRIME]")
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)


# Busca todos os filmes com participação da atriz de nome 'Nicole Balsam'
lista = banco.buscar_por_elenco('Nicole Balsam')
print("[FILMES COM NICOLE BALSAM]")
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.elenco)


# Busca os melhores filmes do ano de 2019
lista = banco.buscar_melhores_do_ano('2019')
print("[FILMES MELHORES DO ANO DE 2019]")
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.avaliacao)


# Exporta filmes do banco de dados para um novo arquivo de texto
banco.exportar_filmes('saida.txt')
