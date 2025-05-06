from models import db, Genero, Album, Musica


def inicializar():
    db.connect()
    db.create_tables([Genero, Album, Musica])


def menu():
    while True:
        print("\n--- CATÁLOGO DE MÚSICA ---")
        print("1 - Adicionar Gênero")
        print("2 - Adicionar Álbum")
        print("3 - Adicionar Música")
        print("4 - Listar Gêneros")
        print("5 - Listar Álbuns")
        print("6 - Listar Músicas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do gênero: ")
            Genero.create(nome=nome)
        elif opcao == "2":
            nome = input("Nome do álbum: ")
            ano = int(input("Ano: "))
            Album.create(nome=nome, ano=ano)
        elif opcao == "3":
            titulo = input("Título da música: ")
            artista = input("Artista: ")
            duracao = int(input("Duração (segundos): "))

            print("\n--- GÊNEROS ---")
            for g in Genero.select():
                print(f"{g.id} - {g.nome}")
            genero_id = int(input("ID do gênero: "))

            print("\n--- ÁLBUNS ---")
            for a in Album.select():
                print(f"{a.id} - {a.nome} ({a.ano})")
            album_id = int(input("ID do álbum: "))

            Musica.create(
                titulo=titulo,
                artista=artista,
                duracao=duracao,
                genero=genero_id,
                album=album_id
            )
        elif opcao == "4":
            for g in Genero.select():
                print(f"{g.id} - {g.nome}")
        elif opcao == "5":
            for a in Album.select():
                print(f"{a.id} - {a.nome} ({a.ano})")
        elif opcao == "6":
            for m in Musica.select():
                print(f"{m.id} - {m.titulo} | {m.artista} | {m.duracao}s | Álbum: {
                      m.album.nome} | Gênero: {m.genero.nome}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    inicializar()
    menu()
