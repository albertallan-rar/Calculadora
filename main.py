from tkinter import *


class Cal:

    def __init__(self):

        self.window = Tk()
        self.window.title('Calc')
        self.window.resizable(0, 0)# A tela altera o tamanho de acordo com os elementos contidos na tela
        #self.window.config(bg='#503382') Cor de fundo

        self.screen_numbers = Entry(self.window, font='arial 20 bold', bg='#503382', fg='white',width=10)
        self.screen_numbers.pack() #fg é para alterar a cor da letra e numero e bg é a cor de fundo

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button_1 = Button(self.frame, bg='orange', bd=0, text='1', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('1'))
        self.button_2 = Button(self.frame, bg='orange', bd=0, text='2', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('2'))
        self.button_3 = Button(self.frame, bg='orange', bd=0, text='3', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('3'))
        self.button_4 = Button(self.frame, bg='orange', bd=0, text='4', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('4'))
        self.button_5 = Button(self.frame, bg='orange', bd=0, text='5', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('5'))
        self.button_6 = Button(self.frame, bg='orange', bd=0, text='6', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('6'))
        self.button_7 = Button(self.frame, bg='orange', bd=0, text='7', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('7'))
        self.button_8 = Button(self.frame, bg='orange', bd=0, text='8', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('8'))
        self.button_9 = Button(self.frame, bg='orange', bd=0, text='9', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('9'))
        self.button_0 = Button(self.frame, bg='orange', bd=0, text='0', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('0'))

        self.button_soma = Button(self.frame, bg='orange', bd=0, text='+', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('+'))
        self.button_sub = Button(self.frame, bg='orange', bd=0, text='-', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('-'))
        self.button_mult = Button(self.frame, bg='orange', bd=0, text='*', font='arial 20 bold', width=2,
                                height=2, command=lambda: self.clique('*'))
        self.button_divisao = Button(self.frame, bg='orange', bd=0, text='/', font='arial 20 bold', width=2,
                               height=2, command=lambda: self.clique('/'))
        self.button_limpar = Button(self.frame, bg='orange', bd=0, text='C', font='arial 20 bold', width=2,
                                     height=2, command= self.clear)
        self.button_result = Button(self.frame, bg='orange', bd=0, text='=', font='arial 20 bold', width=2,
                                    height=2, command= self.resul)

        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_0.grid(row=3, column=0)

        self.button_soma.grid(row=0, column=3)
        self.button_sub.grid(row=1, column=3)
        self.button_mult.grid(row=2, column=3)
        self.button_divisao.grid(row=3, column=3)
        self.button_limpar.grid(row=3, column=2)
        self.button_result.grid(row=3, column=1)

        self.window.mainloop()

    def clique(self, num):
        self.screen_numbers.insert(END, num)

    def clear(self):
        self.screen_numbers.delete(0, END)

    def resul(self):
        resultado = eval(self.screen_numbers.get())
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(resultado))

Cal()
