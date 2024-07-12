import tkinter as tk
from tkinter import ttk


def printCadastro():
    print("nome= %s \nIdade= %d"% (inputNome.get(), inputIdade.get()))



# CONFIGURAÇÕES DA JANELA
janela = tk.Tk()
janela.title("Formulario de cadastro socioeconome")




# Input lab
## Nome
tk.Label(janela,text="Nome").grid(row=0)
inputNome = tk.Entry(janela)
inputNome.grid(row=0, column=1)


## Idade
tk.Label(janela,text="Idade").grid(row=1)
inputIdade = tk.Entry(janela)
inputIdade.grid(row=1, column=1)


T = tk.Text(janela)
T.grid(row=3, column=0)
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")

# BUTÕES
tk.Button(janela, text='Sair', command=janela.quit).grid(row=5,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=printCadastro).grid(row=5,column=1,sticky=tk.W,pady=4)







janela.mainloop()


# FUNCOES
