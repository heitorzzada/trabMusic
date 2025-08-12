from peewee import *

db = SqliteDatabase('musica.db')


class BaseModel(Model):
    class Meta:
        database = db


class Genero(BaseModel):
    nome = CharField(unique=True)


class Album(BaseModel):
    nome = CharField()
    ano = IntegerField()


class Musica(BaseModel):
    titulo = CharField()
    artista = CharField()
    genero = ForeignKeyField(Genero, backref='musicas')
    album = ForeignKeyField(Album, backref='musicas')


# Depois de criar as classes, conecta no banco de dados
db.connect()

# Cria as tabelas para as classes, caso não existam
db.create_tables([Genero, Album, Musica])