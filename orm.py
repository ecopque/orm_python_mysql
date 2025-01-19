# File: /Train/Databases/ORM.py

# ChatGPT Definition: ORM (Object-Relational Mapping) is a mapping technique that allows interaction between an object-oriented application and a relational database. Instead of writing SQL queries manually to access or manipulate data, ORM provides an abstraction layer that lets you work with objects in your code, while the ORM handles the conversion of these objects into SQL queries and the interaction with the database.

# ----------------------------------------------------
# pip install sqlalchemy

# Importação das bibliotecas do SQLAlchemy:
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create_engine: Cria uma conexão com o banco de dados.
# Column: Define uma coluna em uma tabela.
# Integer, String: Tipos de dados para as colunas (inteiro e string).
# declarative_base: Base para as classes de mapeamento ORM, usada para definir as tabelas.
# sessionmaker: Cria uma fábrica de sessões (que é usada para interagir com o banco de dados).

# Definindo a conexão com o banco de dados:
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
DATABASE = 'mariadb_terminal'
PORT = '3306'
# root:123456@localhost:3306/mariadb_terminal
CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Criando a engine e a sessão:
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine) # Return a method.
session = Session()

# Definindo a classe que representa a tabela:
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user = Column(String(25))
    password = Column(String(100))

# ----------------------------------------------------
# Obs: Atualizando ORM.py e ORM2.py.

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category = Column(String(100))

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    product = Column(String(100))
    fk_category = Column(Integer, ForeignKey('category.id'))

# Criando as tabelas no banco de dados:
Base.metadata.create_all(engine)

# ----------------------------------------------------
# Obs: Nesta aula vamos inserir alguns dados pelo terminal;

# Inserindo categoria:
# INSERT INTO category (category) VALUES ('fruits');

# Verificando as categorias inseridas:
# SELECT * FROM category;

# Decidi mudar nome da coluna:
# ALTER TABLE product CHANGE COLUMN id_category fk_category int(11);

# Inserindo produto com categoria:
# INSERT INTO product (product, fk_category) VALUES ('Smartphone', 2);

# Resultado (funcionou):
'''
MariaDB [mariadb_terminal]> SELECT * FROM product;
+----+------------+-------------+
| id | product    | fk_category |
+----+------------+-------------+
|  1 | Smartphone |           2 |
+----+------------+-------------+
1 row in set (0.001 sec)

MariaDB [mariadb_terminal]> SELECT * FROM category;
+----+------------+
| id | category   |
+----+------------+
|  1 | fruits     |
|  2 | eletronics |
+----+------------+
2 rows in set (0.001 sec)

# Verificando todas as tabelas:
# MariaDB [mariadb_terminal]> SHOW TABLES;
+----------------------------+
| Tables_in_mariadb_terminal |
+----------------------------+
| category                   |
| person                     |
| product                    |
+----------------------------+
3 rows in set (0.001 sec)
'''
