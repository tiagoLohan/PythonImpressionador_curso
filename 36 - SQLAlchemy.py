from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono



Base.metadata.create_all(bind=db)


# C - CREATE
# usuario = Usuario("Tiago", "lohan@gmail.com", "123456")
# session.add(usuario)
# session.commit()

# R - READ
usuario_tiago = session.query(Usuario).filter_by(email="lohan@gmail.com").first()


# livro = Livro("Harry Potter", 685, usuario_tiago.id)
# session.add(livro)
# session.commit()

# U - UPDATE
usuario_tiago.nome = "Tiago Lohan"
session.add(usuario_tiago)
session.commit()