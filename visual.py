from models import db, Genero, Album, Musica
import tkinter as tk
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
menu_cad.add_command(label="Criar álbum", command=lambda: frame_album.tkraise())
menu_cad.add_command(label="Editar álbum", command=editar)
menu_cad.add_separator()
menu_cad.add_command(label="Excluir álbum", command=excluir)
menumus.add_cascade(label="Cadastro", menu=menu_cad)

menu_sobre = tk.Menu(menumus,tearoff=False)
menu_sobre.add_command(label="Sobre nós", command=sobre)
menumus.add_cascade(label="Sobre", menu=menu_sobre)
janela.config(menu=menumus)


frame_sobre = tk.Frame(janela)
lb_ola = tk.Label(frame_sobre, text="Desenvolvido Por : ", font=FONTE_NEGRITO)
lb_ola.pack(pady=30)
lb_alo = tk.Label(frame_sobre, text="Guilherme Pereira\nHeitor Pontes ", font=FONTE_PADRAO)
lb_alo.pack(pady=30)
frame_sobre.grid(row=0, column=0, sticky="nesw")

frame_inicio = tk.Frame(janela)
frame_inicio.grid(row=0, column=0, sticky="nesw")

lb_ola = tk.Label(frame_inicio, text="Bem-vindo ao sistema", font=FONTE_NEGRITO)
lb_ola.pack(pady=30)

frame_album = tk.Frame(janela)
frame_album.grid(row=0, column=0, sticky="nesw")


titulo = tk.Label(frame_album, text="VAMOS CRIAR UM ALBUM", font=FONTE_NEGRITO)
titulo.grid(row=0, column=0, columnspan=2, pady=5)

adi = tk.Label(frame_album, text="ADICIONAR O ALBUM", font=FONTE_PADRAO)
adi.grid(row=1, column=0, columnspan=2, pady=5)

a_label = tk.Label(frame_album, text="Nome:", font=FONTE_PADRAO, anchor="w", width=12)
a_label.grid(row=2, column=0, sticky="w", padx=(10, 2), pady=5)

a_entry = tk.Entry(frame_album, width=30)
a_entry.grid(row=2, column=1, sticky="w", padx=(2, 10), pady=5)

ano_label = tk.Label(frame_album, text="Ano:", font=FONTE_PADRAO, width=12, anchor="w")
ano_label.grid(row=3, column=0, sticky="w", padx=(10, 2), pady=5)

ano_entry = tk.Entry(frame_album, width=30)
ano_entry.grid(row=3, column=1, sticky="w", padx=(2, 10), pady=5)

botao_salvar = tk.Button(frame_album, text="SALVAR", font=FONTE_PADRAO, bg="#2196F3", fg="white", command=salvar)
botao_salvar.grid(row=4, column=0, columnspan=2, pady=20)

botao_del = tk.Button(frame_album, text="LIMPAR", font=FONTE_PADRAO, command=limpar)
botao_del.grid(row=4, column=2, columnspan=2, pady=20)

lista_label = tk.Label(frame_album, text="Álbuns cadastrados:", font=FONTE_PADRAO)
lista_label.grid(row=5, column=0, columnspan=3, pady=(10, 5))

lista_albuns = tk.Listbox(frame_album, width=50, height=10)
lista_albuns.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# b_editar = tk.Button(frame_album, text="EDITAR", font=FONTE_PADRAO, bg="green", fg="white", command=editar)
# b_editar.grid(row=7, column=0, pady=10)

# b_excluir = tk.Button(frame_album, text="EXCLUIR", font=FONTE_PADRAO, bg="red", fg="white", command=excluir)
# b_excluir.grid(row=7, column=1, pady=10)

inicio()
carregar_albuns()
janela.mainloop()
