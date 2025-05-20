from models import db, Genero, Album, Musica


def inicializar():
    db.connect()
    db.create_tables([Genero, Album, Musica])


def menu():
    while True:
        print("\n--- CATÁLOGO DE SELEÇÃO ---")
        print("1 - Adicionar ")
        print("2 - Listar ")
        print("3 - Excluir")
        print("4 - Editar")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            while(True):
                print ("\n--- CATALOGO DE ADIÇÃO ---")
                print("1 - Adicionar Gênero")
                print("2 - Adicionar Álbum")
                print("3 - Adicionar Música")
                print("0 - Voltar")
                opcao_1 = input("Escolha: ")
                if opcao_1 == "1":
                    nome = input("Nome do gênero: ")
                    Genero.create(nome=nome)
                elif opcao_1 == "2":
                    nome = input("Nome do álbum: ")
                    ano = int(input("Ano: "))
                    Album.create(nome=nome, ano=ano)
                elif opcao_1 == "3":
                    titulo = input("Título da música: ")
                    artista = input("Artista: ")
                    print("\n--- GÊNEROS ---")
                    print("A MUSICA JA POSSUI GENERO ?\nDIGITE 1 PARA SIM\nDIGITE 2 PARA NÃO")
                    op = input("DIGITE : ")
                    if op == "1":
                        exit
                    elif op == "2":
                        nome = input("Nome do gênero: ")
                        Genero.create(nome=nome)
                    for g in Genero.select():
                        print(f"{g.id} - {g.nome}")
                    genero_id = int(input("ID do gênero: "))
                    genero = Genero.get_by_id(genero_id)
        
                    print("\n--- ÁLBUNS ---")
                    print("A MUSICA JA POSSUI ALBUM ?\nDIGITE 1 PARA SIM\nDIGITE 2 PARA NÃO")
                    opc = input("DIGITE : ")
                    if opc == "1":
                        exit
                    elif opc == "2":
                        nome = input("Nome do álbum: ")
                        ano = int(input("Ano: "))
                        Album.create(nome=nome, ano=ano)
                    for a in Album.select():
                        print(f"{a.id} - {a.nome} ({a.ano})")
                    album_id = int(input("ID do álbum: "))
                    print("Musica criada")
        
                    album = Album.get_by_id(album_id)
        
                    Musica.create(
                        titulo=titulo,
                        artista=artista,
                        genero=genero,
                        album=album
                    )

                elif opcao_1 == "0":
                    print("Saindo...")
                    break 

                else:
                    print("Opcao invalida")

        elif opcao == "2":
            print("\n --- CATALOGO DE LISTAR ---")
            print("1 - Listar Gêneros")
            print("2 - Listar Álbuns")
            print("3 - Listar Músicas")
            opcao_2 = input("Escolha: ")
            if opcao_2 == "1":
                for g in Genero.select():
                    print(f"{g.id} - {g.nome}")
            elif opcao_2 == "2":
                for a in Album.select():
                    print(f"{a.id} - {a.nome} ({a.ano})")
            elif opcao_2 == "3":
                for m in Musica.select():
                        print(f"{m.id} - {m.titulo} | {m.artista} | Álbum: {m.album.nome} | Gênero: {m.genero.nome}")
                        
        elif opcao == "3":
            for m in Musica.select():
                print(f"{m.id} - {m.titulo} | {m.artista} | Álbum: {m.album.nome} | Gênero: {m.genero.nome}")
            ExID = input ("\nInforme o ID da Música que deseja excluir: ")
            mus = Musica.get_by_id(ExID)
            mus.delete_instance()
            print(f"Musica de ID {m.id} excluida com sucesso" )
        
        elif opcao == "4":
            while(True):
                for m in Musica.select():
                    print(f"{m.id} - {m.titulo} | {m.artista} | Álbum: {m.album.nome} | Gênero: {m.genero.nome}")
                MusID = input("\nInforme o ID da Musica que deseja editar: ")
                mus = Musica.get_by_id(MusID)
            
                print(f"\nEditando a música: {mus.titulo} | {mus.artista} | Álbun: {mus.album.nome} | Gênero: {m.genero.nome}")
                print("\nO que deseja editar?")
                print("1 - Título")
                print("2 - Artista")
                print("3 - Gênero")
                print("4 - Álbum")
                print("0 - Cancelar")
                opcao_edicao = input("Escolha: ")
                if opcao_edicao == "1":
                    print(f"Titulo Atual: {mus.titulo}")
                    novo_titulo = input("Novo título: ")
                    mus.titulo = novo_titulo

                elif opcao_edicao == "2":
                    print(f"Artista Atual: {mus.artista}")
                    novo_artista = input("Novo artista: ")
                    mus.artista = novo_artista
                elif opcao_edicao == "3":
                    print("\n--- GÊNEROS ---")
                    for g in Genero.select():
                        print(f"{g.id} - {g.nome}")
                    novo_genero_id = int(input("Novo ID do gênero: "))
                    novo_genero = Genero.get_by_id(novo_genero_id)
                    mus.genero = novo_genero
                elif opcao_edicao == "4":
                    print("\n--- ÁLBUNS ---")
                    for a in Album.select():
                        print(f"{a.id} - {a.nome} ({a.ano})")
                    novo_album_id = int(input("Novo ID do álbum: "))
                    novo_album = Album.get_by_id(novo_album_id)
                    mus.album = novo_album
                elif opcao_edicao == "0":
                    print("Edição cancelada!")
                    break
                else:
                    print("Opção inválida!")
                mus.save()
                print(f"Música de ID {MusID} editada com sucesso!")

        elif opcao == "0":
                    break
        else:
            print("Opção inválida!")    

if __name__ == "__main__":
    inicializar()
    menu()
