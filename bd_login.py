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
    nascimeto = CharField()
    endereco = CharField()
    senha = CharField()

class Duvida(BaseModel):
    nome = CharField()
    email = CharField()
    telefone = CharField()
    duvida = CharField()

if __name__ == "__main__":
    db.connect()
    db.create_tables([Usuario, Duvida])

    #Usuario(nome = "nome", email = "email", telefone = "telefone", nascimento = "nascimento", endereco = "endereco", senha = "senha").save()
    for i in Duvida.select():
        print(i.nome)
