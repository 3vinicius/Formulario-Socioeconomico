from tkinter import messagebox

def centralizarGrid(janela):
    for i in range(6):
        janela.grid_columnconfigure(i, weight=1)
    for i in range(10):
        janela.grid_rowconfigure(i, weight=1)


def exibirDados(varNome,varIdade,varEstadoCivil,varEmpregado,varRefeicaoNaoConsumir, varClassMerenda,varRefeicaoMaisGosta,varRefeicaoMenosGosta):
    print(varNome,varIdade,varEstadoCivil,varEmpregado,varRefeicaoNaoConsumir, varClassMerenda,varRefeicaoMaisGosta,varRefeicaoMenosGosta)

def ValidacaoDeNumeros(inputIdade):
    user_input = inputIdade.get()
    if user_input.isdigit():
        messagebox.showinfo("Resultado", "A entrada contém apenas números.")
    else:
        messagebox.showwarning("Resultado", "A entrada contém caracteres não numéricos.")


def printCadastro(inputNome, inputIdade):
    print("nome= %s \nIdade= %d"% (inputNome.get(), inputIdade.get()))