from tkinter import messagebox

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