import os
from peewee import *

# conexão com o banco de dados do SQLLite
arq = 'cadastro.db'
db = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
        database = db

# declaração da classe herdando características da classe BaseModel

class Usuario(BaseModel):
    # atributos do tipo texto
    nome = CharField()
    email = CharField()
    telefone = CharField()
    nascimento = CharField()
    endereco = CharField()
    senha = CharField()

class Duvida(BaseModel):
    nome = CharField()
    email = CharField()
    telefone = CharField()
    duvida = CharField()
try:
    db.connect()
    db.create_tables([Usuario, Duvida])
except:
    pass
if __name__ == "__main__":
    #Usuario(nome = "nome", email = "email", telefone = "telefone", nascimento = "nascimento", endereco = "endereco", senha = "senha").save()
    print("debug")
    #Duvida(nome = "nome", email = "email", telefone = "telefone", duvida = "duvida").save()
    for i in Duvida.select():
        print(i.nome)
