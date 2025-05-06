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
    duracao = IntegerField()
    genero = ForeignKeyField(Genero, backref='musicas')
    album = ForeignKeyField(Album, backref='musicas')
