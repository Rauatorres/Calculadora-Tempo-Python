from tkinter import *
from TimeCalculator import Time

#   Criando a janela
window = Tk()
window.title('Calculadora de Tempo')
window.geometry('450x180')

#   Quantidade de tempo que será usada como base da operação
hours_base = Entry(window, width=7)
minutes_base = Entry(window, width=7)
seconds_base = Entry(window, width=7)
hours_base.grid(row=1, column=0, pady=3, padx=10)
minutes_base.grid(row=1, column=2, padx=10)
seconds_base.grid(row=1, column=4, padx=10)
Label(window, text=':').grid(row=1, column=1)
Label(window, text=':').grid(row=1, column=3)
hours_base.insert(0, 0)
minutes_base.insert(0, 0)
seconds_base.insert(0, 0)

#   Quantidade de tempo que será adicionada ou subtraída da base
hours_operation = Entry(window, width=7)
minutes_operation = Entry(window, width=7)
seconds_operation = Entry(window, width=7)
hours_operation.grid(row=2, column=0, pady=20, padx=10)
minutes_operation.grid(row=2, column=2, padx=10)
seconds_operation.grid(row=2, column=4, padx=10)
Label(window, text=':').grid(row=2, column=1)
Label(window, text=':').grid(row=2, column=3)
hours_operation.insert(0, 0)
minutes_operation.insert(0, 0)
seconds_operation.insert(0, 0)

#   Texto para indicar o que deve ser escrito nos campos de usuário
Label(window, text='H', pady=5).grid(row=0, column=0)
Label(window, text='Min').grid(row=0, column=2)
Label(window, text='Seg').grid(row=0, column=4)

#   Texto indicando o espaço reservado para mostrar o resultado
Label(window, text='Resultado', pady=10, padx=20, font=('Arial', 13)).grid(row=1, column=5)


#   Função que irá realizar as operações
def operate(type):
    time_operand = Time(hours_base.get(), minutes_base.get(), seconds_base.get())
    if type == '+':
        time_operand.add(hours_operation.get(), minutes_operation.get(), seconds_operation.get())
    elif type == '-':
        time_operand.sub(hours_operation.get(), minutes_operation.get(), seconds_operation.get())
    #   Exibindo o resultado na tela
    Label(window, text=f'{time_operand.get()}',
          font=('Arial', 13), foreground='#006D00').grid(row=1, column=5, rowspan=2)


#   Botões de soma e subtração
sum_button = Button(window, text='+', padx=20, borderwidth=3, font=('Arial', 14),
                    command=lambda: operate('+'))
sub_button = Button(window, text='-', padx=20, borderwidth=3, font=('Arial', 14),
                    command=lambda: operate('-'))
sum_button.grid(row=3, column=0, columnspan=3)
sub_button.grid(row=3, column=2, columnspan=3)

window.mainloop()
