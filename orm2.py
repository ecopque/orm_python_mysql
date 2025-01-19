# File: /Train/Databases/ORM2.py

# ----------------------------------------------------

# Importações e Definição de Função para Obter Sessão:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Person
from sqlalchemy import or_

# Define uma função que cria e retorna uma nova sessão do SQLAlchemy:
def returnsession():
    USER = 'root'
    PASSWORD = '123456'
    HOST = 'localhost'
    DATABASE = 'mariadb_terminal'
    PORT = '3306'
    CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine) # Return a method.
    return Session()

# Criando Instâncias de Person:
session = returnsession()
# new_person = Person(name = 'Edson', 
#                     user='ecop', 
#                     password='123456') # Comentado para aula 1-4.

# new_person2 = Person(name = 'Théo', 
#                     user='thetheo', 
#                     password='123456')

# Adicionando Novas Instâncias à Sessão:
# session.add_all([new_person, new_person2, new_person3]) # Adding multiple.
# session.add(new_person)
# session.add(new_person2) # Comentado para aula 1-4.

# Commitando a Transação:
# session.commit()

# ----------------------------------------------------
# Limpando a Sessão (Rollback):
# session.rollback() # Returning to how it was before. In this case, 'session.add(new_person2)'. # Comentado para aula 1-4.
# session.commit() # Comentado para aula 1-4.

# ----------------------------------------------------
'''
MariaDB [mariadb_terminal]> SELECT * FROM Person;
+----+-------+---------+----------+
| id | name  | user    | password |
+----+-------+---------+----------+
|  1 | Edson | ecop    | 123456   |
|  2 | Théo  | thetheo | 123456   |
|  3 | Théo  | thetheo | 123456 
'''
x = session.query(Person) # class Person().
y = x.all()
print(y) # Response: [<ORM.Person object at 0x7f271bcb5f10>, <ORM.Person object at 0x7f271bcb5f90>, <ORM.Person object at 0x7f271bcb6010>].
print(y[0].id) # Response: 1.
print(y[0].name) # Response: Edson.
print(y[1].name) # Response: Théo.

for i1 in y:
    print(i1.name) # Response: Edson, Théo, Théo.

z = session.query(Person).filter(Person.name == 'Théo')
# z = session.query(Person).filter(Person.name == 'Théo').filter(Person.user == 'thetheo')
# z = session.query(Person).filter_by(name = 'Théo', user = 'thetheo')
for i2 in z:
    print(i2.id) # Response: 2, 3.

# ----------------------------------------------------

x = session.query(Person).filter(or_(Person.name == 'Edson', Person.user == 'ecop')).all()
for i3 in x:
    print(i3.id) # Response: 1.

# ----------------------------------------------------

x = session.query(Person).filter(Person.id == 1).all()
x[0].name = 'Edson New' # Alterando nome.
x[0].password += x[0].password + '999' # Adicionando caracteres à senha.
session.commit()

# ----------------------------------------------------

# x = session.query(Person).filter(Person.id == 1).delete() # Irá deletar toda linha de id 1.
# session.commit()

# x = session.query(Person).filter(Person.id == 3).one() # Seleciona apenas um.
# session.delete(x)
# session.commit()

# ----------------------------------------------------
# Obs: Atualizando ORM.py e ORM2.py.
