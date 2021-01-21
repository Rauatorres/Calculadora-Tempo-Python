from tkinter import *

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
    try:
        #   Capturando os inputs do usuário
        hours_base_operating = int(hours_base.get())
        minutes_base_operating = int(minutes_base.get())
        seconds_base_operating = int(seconds_base.get())
        hours_operation_operating = int(hours_operation.get())
        minutes_operation_operating = int(minutes_operation.get())
        seconds_operation_operating = int(seconds_operation.get())

        #   Para retornar erro quando for digitado algum valor negativo
        if hours_base_operating < 0 or minutes_base_operating < 0 or seconds_base_operating < 0:
            raise ValueError
        if hours_operation_operating < 0 or minutes_operation_operating < 0 or seconds_operation_operating < 0:
            raise ValueError

        #   Efetuando uma operação de acordo com o tipo de operação escolhido (soma ou subtração)
        if type == '+':
            hours_result = hours_base_operating + hours_operation_operating
            minutes_result = minutes_base_operating + minutes_operation_operating
            seconds_result = seconds_base_operating + seconds_operation_operating
            if seconds_result >= 60:
                minutes_result += seconds_result // 60
                seconds_result %= 60
            if minutes_result >= 60:
                hours_result += minutes_result // 60
                minutes_result %= 60
        else:
            hours_result = hours_base_operating - hours_operation_operating
            minutes_result = minutes_base_operating - minutes_operation_operating
            seconds_result = seconds_base_operating - seconds_operation_operating
            if seconds_result < 0:
                minutes_result += seconds_result // 60
                seconds_result %= 60
            if minutes_result < 0:
                hours_result += minutes_result // 60
                minutes_result %= 60
            if hours_result < 0:
                raise ValueError

        #   Exibindo o resultado na tela
        Label(window, text=f'{hours_result}:{minutes_result}:{seconds_result}',
              font=('Arial', 13), foreground='#006D00').grid(row=1, column=5, rowspan=2)
    except ValueError:
        Label(window, text=f'Erro -\nValores digitados inválidos',
              font=('Arial', 13), foreground='#FF0000').grid(row=1, column=5, rowspan=2)


#   Botões de soma e subtração
sum_button = Button(window, text='+', padx=20, borderwidth=3, font=('Arial', 14),
                    command=lambda: operate('+'))
sub_button = Button(window, text='-', padx=20, borderwidth=3, font=('Arial', 14),
                    command=lambda: operate('-'))
sum_button.grid(row=3, column=0, columnspan=3)
sub_button.grid(row=3, column=2, columnspan=3)

window.mainloop()
