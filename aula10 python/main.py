from tkinter import *

janela = Tk()
janela.title("Maior dos números")
janela.geometry("400x400")



def checar_maior():
    numero1 = float(numero1_input.get())
    numero2 = float(numero2_input.get())

    if numero1 > numero2:
        resultado.configure(text=f"O {numero1} é o maior")
    elif numero2 > numero1:
        resultado.configure(text=f"O {numero2} é o maior")
    else:
        resultado.configure(text=f"São iguais")


numero1_label = Label(text="Digite o primeiro número").pack()
numero1_input = Entry()
numero1_input.pack()



numero2_label = Label(text="Digite o segundo número").pack()
numero2_input = Entry()
numero2_input.pack()



botao = Button(janela, text="Checar maior", command=checar_maior)
botao.pack()

resultado = Label(text="")
resultado.pack()

janela.mainloop()





