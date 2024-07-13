import tkinter as tk
from tkinter import ttk

from funções import *

# CONFIGURAÇÕES DA JANELA
janela = tk.Tk()
janela.title("Formulario de cadastro socioeconome")




# Input lab
## Nome
varNome = tk.StringVar()
tk.Label(janela,text="Nome").grid(row=0)
inputNome = tk.Entry(janela, width = 30, textvariable=varNome)
inputNome.grid(row=0, column=1)


## Idade
varIdade = tk.StringVar()
tk.Label(janela,text="Idade").grid(row=0,column=2)
inputIdade = tk.Entry(janela, textvariable=varIdade, width = 30)
inputIdade.grid(row=0, column=3)


## Estado Civil
tk.Label(janela,text="Estado Civil").grid(row=1)
varEstadoCivil = tk.StringVar()
estadoCivil = ttk.Combobox(janela, width = 27, textvariable =varEstadoCivil)
# Adição de itens no Combobox
estadoCivil['values'] = ('Casado (a)', 'Solteiro (a)')
estadoCivil.grid(column = 1, row = 1)
estadoCivil.current()


## Número de Filhos
varNumFilhos = tk.StringVar()
tk.Label(janela,text="Número de Filhos").grid(row=1,column=2)
inputNumFilhos = tk.Entry(janela, textvariable=varNumFilhos, width=30)
inputNumFilhos.grid(row=1, column=3)


## Sexo
tk.Label(janela,text="Sexo").grid(row=2)
varSexo = tk.StringVar()
inputSexo = ttk.Combobox(janela, width = 27, textvariable =varSexo)
# Adição de itens no Combobox
inputSexo['values'] = ('Masculino', 'Feminino')
inputSexo.grid(column = 1, row = 2)
inputSexo.current()

## Você está empregado ?
tk.Label(janela,text="Voce Está empregado").grid(row=2,column=2)
varEmpregado = tk.StringVar()
inputEmpregado = ttk.Combobox(janela, width = 27, textvariable =varEmpregado)
# Adição de itens no Combobox
inputEmpregado['values'] = ('Sim', 'Não')
inputEmpregado.grid(column = 3, row = 2)
inputEmpregado.current()

## Qual refeição voce não pode consumir
tk.Label(janela,text="Qual refeição voce não pode consumir").grid(row=3)
varRefeicaoNaoConsumir = tk.StringVar()
inputRefeicaoNaoConsumir = ttk.Combobox(janela, width = 27, textvariable =varRefeicaoNaoConsumir)
# Adição de itens no Combobox
inputRefeicaoNaoConsumir['values'] = ('Cuscuz com carne moida', 'Cuscuz com fígado','Cuscuz com leite','Manguzá',
                            'Macarrão com carne moida','Sopa','Arroz com Strogonoff','Arroz com carne moida','NENHUMA')
inputRefeicaoNaoConsumir.grid(column = 1, row = 3)
inputRefeicaoNaoConsumir.current()

## Classificação da merenda
tk.Label(janela,text="Classificação da merenda").grid(row=3,column=2)
varClassMerenda = tk.StringVar()
inputClassMerenda = ttk.Combobox(janela, width = 27, textvariable =varClassMerenda)
# Adição de itens no Combobox
inputClassMerenda['values'] = ('1', '2','3','4','5','6','7','8','9','10')
inputClassMerenda.grid(column = 3, row = 3)
inputClassMerenda.current()

## Qual Refeição voçê não gosta
tk.Label(janela,text="Qual Refeição voçê mais gosta").grid(row=4)
varRefeicaoMaisGosta = tk.StringVar()
inputRefeicaMaisGosta = ttk.Combobox(janela, width = 27, textvariable =varRefeicaoMaisGosta)
# Adição de itens no Combobox
inputRefeicaMaisGosta['values'] = ('Cuscuz com carne moida', 'Cuscuz com fígado', 'Cuscuz com leite', 'Manguzá',
                                   'Macarrão com carne','Arroz com Strogonoff','Arroz com carne moida','NENHUMA'
                                   'Sopa')
inputRefeicaMaisGosta.grid(column = 1, row = 4)
inputRefeicaMaisGosta.current()



## Qual a Refeição voce menos gosta
tk.Label(janela,text="Qual Refeição voçê menos gosta").grid(row=4,column=2)
varRefeicaoMenosGosta = tk.StringVar()
inputRefeicaoMenosGosta = ttk.Combobox(janela, width = 27, textvariable =varRefeicaoMenosGosta)
# Adição de itens no Combobox
inputRefeicaoMenosGosta['values'] = ('Cuscuz com carne moida', 'Cuscuz com fígado','Cuscuz com leite','Manguzá',
                                     'Macarrão com carne moida','Sopa','Arroz com Strogonoff','Arroz com carne moida'
                                     ,'NENHUMA')
inputRefeicaoMenosGosta.grid(column = 3, row = 4)
inputRefeicaoMenosGosta.current()

# BUTÕES
tk.Button(janela, text='Sair', command=janela.quit).grid(row=8,column=0,sticky=tk.W,pady=4)
(tk.Button(janela, text='Exibir Dados', command=exibirDados(varNome,varIdade,varEstadoCivil,varEmpregado,
                                                           varRefeicaoNaoConsumir, varClassMerenda,varRefeicaoMaisGosta,
                                                           varRefeicaoMenosGosta))
 .grid(row=8,column=1,sticky=tk.W,pady=4))



janela.mainloop()


# FUNCOES
