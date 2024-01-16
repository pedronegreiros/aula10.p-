from tkinter import *

janela = Tk()
janela.title("semáforo")
janela.geometry("400x400")

def selecionar_cor():
    hora_trabalhada = float(salario_input.get())/float(hora_input.get())
    if hora_trabalhada < 11:
         resultado.configure(text = f'{hora_trabalhada}', bg="#f01010")
    elif hora_trabalhada <26:
         resultado.configure(text = f"{hora_trabalhada}", bg="#ea650c")
    elif hora_trabalhada < 51:
         resultado.configure(text = f"{hora_trabalhada}", bg="#0c24ea")
    else:
         resultado.configure(text = f"{hora_trabalhada}", bg="#bf2ed6")


salario_label = Label(text="Digite seu salario").pack()
salario_input = Entry()
salario_input.pack()


hora_label = Label(text="quantas horas você trabalha").pack()
hora_input = Entry()
hora_input.pack()

resultado = Label(text = "")
resultado.pack()

botao1 = Button(janela, text="selecione cor", command=selecionar_vermelho)
botao1.pack()
botao2 = Button(janela, text="selecione cor", command=selecionar_amarelo)
botao2.pack()
botao3 = Button(janela, text="selecione cor", command=selecionar_verde)
botao3.pack()

janela.mainloop()






janela.mainloop()
