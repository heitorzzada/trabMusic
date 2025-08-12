from models import db, Genero, Album, Musica
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

def salvar():
    nome = a_entry.get()

    try:
        ano = ano_entry.get()
        ano = int(ano)
    except:
        messagebox.showerror("Erro", "Ano inválido")
        return

    if len(nome) > 0:

            Album.create(nome=nome, ano=ano)
            messagebox.showinfo("Sucesso", f"Álbum '{nome}' salvo com sucesso!") 
     
    else:
        messagebox.showerror("Atenção", "Informe o nome do álbum")


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


botao_salvar = tk.Button(janela, text="Salvar", font=FONTE_PADRAO, command=salvar)
botao_salvar.grid(row=4, column=0, columnspan=2, pady=20)

botao_del = tk.Button(janela, text="LIMPAR", font=FONTE_PADRAO)
botao_del.grid(row=4, column=2, columnspan=2, pady=20)

janela.mainloop()