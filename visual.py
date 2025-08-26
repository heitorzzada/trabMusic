from models import db, Genero, Album, Musica
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

ob_Album = None

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
    except:
        messagebox.showerror("Erro", "Ano inválido")
        return

    if len(nome) > 0:

        if (ob_Album is None):
            Album.create(nome=nome, ano=ano)
        else :
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
        # nome = a_entry.get()
        # ano = int(ano_entry.get())
    except:
        messagebox.showerror("Erro", "ID inválido.")
        return


    album = Album.get_by_id(album_id)

    a_entry.insert(0, album.nome)
    ano_entry.insert(0,album.ano)

    global ob_Album
    ob_Album = album
    # album.save()

    # messagebox.showinfo("Sucesso", "Álbum atualizado com sucesso!")
    # limpar()
    # carregar_albuns()

FONTE_PADRAO = ("Arial", 12)
FONTE_NEGRITO = ("Arial", 20, "bold")
janela.geometry("500x500")

titulo = tk.Label(janela, text="VAMOS CRIAR UM ALBUM", font=FONTE_NEGRITO)
titulo.grid(row=0, column=0, columnspan=2, pady=5)

adi = tk.Label(janela, text="ADICIONAR O ALBUM", font=FONTE_PADRAO)
adi.grid(row=1, column=0, columnspan=2, pady=5)

a_label = tk.Label(janela, text="Nome:", font=FONTE_PADRAO, anchor="w", width=12)
a_label.grid(row=2, column=0, sticky="w", padx=(10,2), pady=5)

a_entry = tk.Entry(janela, width=30)
a_entry.grid(row=2, column=1, sticky="w", padx=(2,10), pady=5)

ano_label = tk.Label(janela, text="Ano:", font=FONTE_PADRAO, width=12, anchor="w")
ano_label.grid(row=3, column=0, sticky="w", padx=(10,2), pady=5)
ano_entry = tk.Entry(janela, width=30)
ano_entry.grid(row=3, column=1, sticky="w", padx=(2,10), pady=5)

botao_salvar = tk.Button(janela, text="SALVAR", font=FONTE_PADRAO,bg ="#2196F3", fg= "white", command=salvar)
botao_salvar.grid(row=4, column=0, columnspan=2, pady=20)

botao_del = tk.Button(janela, text="LIMPAR", font=FONTE_PADRAO, command=limpar)
botao_del.grid(row=4, column=2, columnspan=2, pady=20)

lista_label = tk.Label(janela, text="Álbuns cadastrados:", font=FONTE_PADRAO)
lista_label.grid(row=5, column=0, columnspan=3, pady=(10,5))

lista_albuns = tk.Listbox(janela, width=50, height=10)
lista_albuns.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

b_editar = tk.Button(janela, text="EDITAR", font=FONTE_PADRAO,bg = "green", fg = "white", command=editar)
b_editar.grid(row=7, column=0, pady=10)

b_excluir = tk.Button(janela, text="EXCLUIR", font=FONTE_PADRAO,bg = "red", fg = "white", command=excluir)
b_excluir.grid(row=7, column=1, pady=10)

carregar_albuns() 
janela.mainloop()
