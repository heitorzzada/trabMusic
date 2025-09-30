from models import db, Genero, Album, Musica
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

janela = tk.Tk()
menumus = tk.Menu(janela)

ob_Album = None

def clicar():
    print("menu clicar")
    messagebox.showinfo("Info", "Essa é a mensagem")

def inicio():
    frame_inicio.tkraise()
def sobre():
    frame_sobre.tkraise()
def limpar():
    a_entry.delete(0, tk.END)
    ano_entry.delete(0, tk.END)

def carregar_albuns():
    lista_albuns.delete(0, tk.END) 
    for album in Album.select():
        lista_albuns.insert(tk.END, f"{album.id} - {album.nome} ({album.ano})")

def salvar():


    global ob_Album

    nome = a_entry.get()
    
    try:
        ano = ano_entry.get()
        ano = int(ano)
    except ValueError:
        messagebox.showerror("Erro", "Ano inválido")
        return

    if len(nome) > 0:
        if ob_Album is None:
            Album.create(nome=nome, ano=ano)
        else:
            ob_Album.nome = nome 
            ob_Album.ano = ano
            ob_Album.save()
            ob_Album = None

        messagebox.showinfo("Sucesso", f"Álbum '{nome}' salvo com sucesso!") 
        limpar()
        carregar_albuns()  
    else:
        messagebox.showerror("Atenção", "Informe o nome do álbum")

def excluir():
    selecao = lista_albuns.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione um álbum para excluir.")
        return

    item = lista_albuns.get(selecao)
    album_id = int(item.split(" - ")[0])

    album = Album.get_or_none(Album.id == album_id)
    if album:
        if messagebox.askyesno("Confirmar", f"Deseja excluir o álbum '{album.nome}'?"):
            album.delete_instance()
            carregar_albuns()
            limpar()

def editar():
    selecao = lista_albuns.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione um álbum para atualizar.")
        return

    item = lista_albuns.get(selecao[0])
    try:
        album_id = int(item.split(" - ")[0])
    except ValueError:
        messagebox.showerror("Erro", "ID inválido.")
        return

    album = Album.get_by_id(album_id)

    a_entry.delete(0, tk.END)
    ano_entry.delete(0, tk.END)

    a_entry.insert(0, album.nome)
    ano_entry.insert(0, album.ano)

    global ob_Album
    ob_Album = album


def salvar_gen():
    nome_genero = a_entry_gen.get()

    if not nome_genero:
        messagebox.showerror("Erro", "Informe o nome do gênero.")
        return

    if Genero.select().where(Genero.nome == nome_genero).exists():
        messagebox.showwarning("Aviso", f"O gênero '{nome_genero}' já existe.")
        return

    Genero.create(nome=nome_genero)
    messagebox.showinfo("Sucesso", f"Gênero '{nome_genero}' salvo com sucesso!")
    a_entry_gen.delete(0, tk.END)
    carregar_generos()


def excluir_gen():
    selecao = lista_albuns_gen.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione um gênero para excluir.")
        return

    item = lista_albuns_gen.get(selecao[0])
    genero_id = int(item.split(" - ")[0])

    genero = Genero.get_or_none(Genero.id == genero_id)
    if genero:
        if messagebox.askyesno("Confirmar", f"Deseja excluir o gênero '{genero.nome}'?"):
            genero.delete_instance()
            carregar_generos()
            a_entry_gen.delete(0, tk.END)


def carregar_generos():
    lista_albuns_gen.delete(0, tk.END)
    for gen in Genero.select():
        lista_albuns_gen.insert(tk.END, f"{gen.id} - {gen.nome}")
Musica
def salvar_art():
    nome_art = a_entry_art.get()

    if not nome_art:
        messagebox.showerror("Erro", "Informe o nome do gênero.")
        return

    if Musica.select().where(Musica.titulo == nome_art).exists():
        messagebox.showwarning("Aviso", f"A Musica '{nome_art}' já existe.")
        return

    Musica.create(nome=nome_art)
    messagebox.showinfo("Sucesso", f"Gênero '{nome_art}' salvo com sucesso!")
    a_entry_art.delete(0, tk.END)
    carregar_art()

def excluir_art():
    selecao = lista_albuns_art.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione um gênero para excluir.")
        return

    item = lista_albuns_art.get(selecao[0])
    art_id = int(item.split(" - ")[0])

    art = Musica.get_or_none(Musica.id == art_id)
    if art:
        if messagebox.askyesno("Confirmar", f"Deseja excluir o gênero '{art.nome}'?"):
            art.delete_instance()
            carregar_art()
            a_entry_art.delete(0, tk.END)

def carregar_art():
    lista_albuns_art.delete(0, tk.END)
    for art in Musica.select():
        lista_albuns_art.insert(tk.END, f"{art.id} - {art.nome}")

def carregar_generos_combobox():
    generos = [gen.nome for gen in Genero.select()]
    genero_combobox['values'] = generos
 

def carregar_album_combobox():
    albuns = [a.nome for a in Album.select()]
    album_combobox['values'] = albuns
    


FONTE_PADRAO = ("Arial", 12)
FONTE_NEGRITO = ("Arial", 20, "bold")
janela.geometry("500x500")


menumus = tk.Menu(janela)

menu_arquivo = tk.Menu(menumus, tearoff=False)
menu_arquivo.add_command(label="Início", command=inicio)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)
menumus.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_cad = tk.Menu(menumus, tearoff=False)
menu_cad.add_command(label="Album", command=lambda: frame_album.tkraise())
menu_cad.add_command(label="Genero", command=lambda: frame_gen.tkraise())
menu_cad.add_command(label="Musica", command=lambda: frame_art.tkraise())
menu_cad.add_separator()
menu_cad.add_command(label="Listar itens", command=sobre)
menumus.add_cascade(label="Cadastro", menu=menu_cad)

menu_sobre = tk.Menu(menumus,tearoff=False)
menu_sobre.add_command(label="Sobre nós", command=sobre)
menumus.add_cascade(label="Sobre", menu=menu_sobre)
janela.config(menu=menumus)


frame_sobre = tk.Frame(janela,bg="#e6f2ff")
lb_ola = tk.Label(frame_sobre, text="Desenvolvido Por : ", font=FONTE_NEGRITO,bg = "#e6f2ff")
lb_ola.pack(pady=30)
lb_alo = tk.Label(frame_sobre, text="Guilherme Pereira\nHeitor Pontes ", font=FONTE_PADRAO,bg = "#e6f2ff")
lb_alo.pack(pady=30)
frame_sobre.grid(row=0, column=0, sticky="nesw")




frame_inicio = tk.Frame(janela)
frame_inicio.grid(row=0, column=0, sticky="nesw")

lb_ola = tk.Label(frame_inicio, text="Bem-vindo ao sistema", font=FONTE_NEGRITO)
lb_ola.pack(pady=30)




frame_album = tk.Frame(janela, bg="black")
frame_album.grid(row=0, column=0, sticky="nesw")


titulo = tk.Label(frame_album, text="VAMOS CRIAR UM ALBUM", font=FONTE_NEGRITO,fg="white", bg="black")
titulo.grid(row=0, column=0, columnspan=2, pady=5)

adi = tk.Label(frame_album, text="ADICIONAR O ALBUM", font=FONTE_PADRAO,fg="#39FF14", bg="black")
adi.grid(row=1, column=0, columnspan=2, pady=5)

a_label = tk.Label(frame_album, text="Nome:", font=FONTE_PADRAO, anchor="w", width=12,fg="#39FF14", bg="black")
a_label.grid(row=2, column=0, sticky="w", padx=(10, 2), pady=5)

a_entry = tk.Entry(frame_album, width=30,fg="WHITE", bg="black")
a_entry.grid(row=2, column=1, sticky="w", padx=(2, 10), pady=5)

ano_label = tk.Label(frame_album, text="Ano:", font=FONTE_PADRAO, width=12, anchor="w",fg="#39FF14", bg="black")
ano_label.grid(row=3, column=0, sticky="w", padx=(10, 2), pady=5)

ano_entry = tk.Entry(frame_album, width=30,fg="WHITE", bg="black")
ano_entry.grid(row=3, column=1, sticky="w", padx=(2, 10), pady=5)



botao_salvar = tk.Button(frame_album, text="SALVAR", font=FONTE_PADRAO, bg="green", fg="white", command=salvar)
botao_salvar.grid(row=5, column=0, columnspan=2, pady=20)

botao_del = tk.Button(frame_album, text="LIMPAR", font=FONTE_PADRAO, command=limpar)
botao_del.grid(row=5, column=2, columnspan=2, pady=20)

lista_label = tk.Label(frame_album, text="Álbuns cadastrados:", font=FONTE_PADRAO, fg="#39FF14", bg="black")
lista_label.grid(row=6, column=0, columnspan=3, pady=(10, 5))

lista_albuns = tk.Listbox(frame_album, width=50, height=10,fg="WHITE", bg="black")
lista_albuns.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

b_editar = tk.Button(frame_album, text="EDITAR", font=FONTE_PADRAO, bg="green", fg="white", command=editar)
b_editar.grid(row=7, column=0, pady=10)

b_excluir = tk.Button(frame_album, text="EXCLUIR", font=FONTE_PADRAO, bg="red", fg="white", command=excluir)
b_excluir.grid(row=7, column=1, pady=10)


#######################################################################

frame_gen = tk.Frame(janela, bg="black")
frame_gen.grid(row=0, column=0, sticky="nesw")


titulo_gen = tk.Label(frame_gen, text="VAMOS ADICIONAR UM GENERO", font=FONTE_NEGRITO,fg="white", bg="black")
titulo_gen.grid(row=0, column=0, columnspan=2, pady=5)

adi_gen = tk.Label(frame_gen, text="ADICIONAR O GENERO", font=FONTE_PADRAO,fg="#39FF14", bg="black")
adi_gen.grid(row=1, column=0, columnspan=2, pady=5)

a_label_gen = tk.Label(frame_gen, text="Nome:", font=FONTE_PADRAO, anchor="w", width=12,fg="#39FF14", bg="black")
a_label_gen.grid(row=2, column=0, sticky="w", padx=(10, 2), pady=5)

a_entry_gen = tk.Entry(frame_gen, width=30,fg="WHITE", bg="black")
a_entry_gen.grid(row=2, column=1, sticky="w", padx=(2, 10), pady=5)


botao_salvar_gen = tk.Button(frame_gen, text="SALVAR", font=FONTE_PADRAO, bg="green", fg="white", command=salvar_gen)
botao_salvar_gen.grid(row=5, column=0, columnspan=2, pady=20)

botao_ex_gen = tk.Button(frame_gen, text="EXCLUIR", font=FONTE_PADRAO, command=excluir_gen)
botao_ex_gen.grid(row=5, column=1 ,columnspan=2, pady=20)

lista_label_gen = tk.Label(frame_gen, text="Generos cadastrados:", font=FONTE_PADRAO, fg="#39FF14", bg="black")
lista_label_gen.grid(row=6, column=0, columnspan=3, pady=(10, 5))

lista_albuns_gen = tk.Listbox(frame_gen, width=50, height=10,fg="WHITE", bg="black")
lista_albuns_gen.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

###################################################################################

frame_art = tk.Frame(janela, bg="black")
frame_art.grid(row=0, column=0, sticky="nesw")

titulo_art = tk.Label(frame_art, text="VAMOS ADICIONAR UMA MUSICA", font=FONTE_NEGRITO, fg="white", bg="black")
titulo_art.grid(row=0, column=0, columnspan=2, pady=5)

adi_art = tk.Label(frame_art, text="ADICIONAR A MUSICA", font=FONTE_PADRAO, fg="#39FF14", bg="black")
adi_art.grid(row=1, column=0, columnspan=2, pady=5)

a_label_gen = tk.Label(frame_art, text="Genero:", font=FONTE_PADRAO, anchor="w", width=12, fg="#39FF14", bg="black")
a_label_gen.grid(row=2, column=0, sticky="w", padx=(10, 2), pady=5)

genero_combobox=ttk.Combobox(frame_art,values=[""])
carregar_generos_combobox()
genero_combobox.grid(row=2, column=1, sticky="w", padx=(10, 2), pady=5)

a_label_album = tk.Label(frame_art, text="Album:", font=FONTE_PADRAO, anchor="w", width=12, fg="#39FF14", bg="black")
a_label_album.grid(row=3, column=0, sticky="w", padx=(10, 2), pady=5)

album_combobox=ttk.Combobox(frame_art,values=[""])
carregar_album_combobox()
album_combobox.grid(row=3, column=1, sticky="w", padx=(10, 2), pady=5)

a_label_titu = tk.Label(frame_art, text="TITULO:", font=FONTE_PADRAO, anchor="w", width=12, fg="#39FF14", bg="black")
a_label_titu.grid(row=4, column=0, sticky="w", padx=(10, 2), pady=5)

a_entry_tit = tk.Entry(frame_art, width=30, fg="WHITE", bg="black")
a_entry_tit.grid(row=4, column=1, sticky="w", padx=(2, 10), pady=5)

botao_salvar_art = tk.Button(frame_art, text="SALVAR", font=FONTE_PADRAO, bg="green", fg="white", command=salvar_art)
botao_salvar_art.grid(row=5, column=0, columnspan=2, pady=20)

botao_ex_art = tk.Button(frame_art, text="EXCLUIR", font=FONTE_PADRAO, command=excluir_art)
botao_ex_art.grid(row=5, column=1, columnspan=2, pady=20)

lista_label_art = tk.Label(frame_art, text="Musicas cadastradas:", font=FONTE_PADRAO, fg="#39FF14", bg="black")
lista_label_art.grid(row=6, column=0, columnspan=3, pady=(10, 5))

lista_albuns_art = tk.Listbox(frame_art, width=50, height=10, fg="WHITE", bg="black")
lista_albuns_art.grid(row=7, column=0, columnspan=3, padx=10, pady=5)



genero_label = tk.Label(frame_album, text="Gênero:", font=FONTE_PADRAO, anchor="w", width=12,fg="#39FF14", bg="black")
genero_label.grid(row=4, column=0, sticky="w", padx=(10, 2), pady=5)

 

inicio()
carregar_albuns()
carregar_generos()
carregar_art()
carregar_generos_combobox()
janela.mainloop()
