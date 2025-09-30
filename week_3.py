import FreeSimpleGUI as sg
from decimal import Decimal, getcontext

getcontext().prec = 10

def color_button(name):
    for i in ["-DIVIDED-", "-TIMES-", "-MINUS-", "-PLUS-"]:
        if i == name:
            window[f"{i}"].update(button_color=("#FFA500", "white"))
        else:
            window[f"{i}"].update(button_color=("white", "#FFA500"))
def equal(sign):
    global current_value, current_value_2
    if sign == "+":
        summ =  str(float(current_value_2) + float(current_value))
        window['-OUT_1-'].update(print_current(summ))
        current_value, current_value_2 = f'{summ}', ''
    elif sign == "÷":
        summ =  str(float(current_value_2) / float(current_value))
        window['-OUT_1-'].update(print_current(summ))
        current_value, current_value_2 = f'{summ}', ''

    elif sign == "x":
        summ =  str(float(current_value_2) * float(current_value))
        window['-OUT_1-'].update(print_current_for_minus_or_plus(summ))
        current_value, current_value_2 = f'{summ}', ''

    elif sign == "-":
        summ =  str(float(current_value_2) - float(current_value))
        window['-OUT_1-'].update(print_current_for_minus_or_plus(summ))
        current_value, current_value_2 = f'{summ}', ''

def print_current(value: str) -> str:
    """Формат для процентов и простых случаев"""
    num = Decimal(value)
    return format(num, 'f').rstrip('0').rstrip('.')

def print_current_for_minus_or_plus(value):
    return f"{Decimal(value):f}".rstrip('0').rstrip('.')

def print_current_for_procent(value):
    return str(Decimal(value).normalize())

    
sg.set_options(use_ttk_buttons=False)
layout = [
    [sg.Text("", size=(100, 1), font=("ARIAL", 50),  key="-OUT_1-", background_color = 'black', justification = "right")],
    [sg.Button('AC',size = (7, 1.2), font=("ARIAL", 19),  button_color = ('black','#F0F8FF')),
     sg.Button('+/-', size = (7, 1.2), font=("ARIAL", 19), button_color = ('black','#F0F8FF')),
     sg.Button('%', size = (7, 1.2), font=("ARIAL", 19), button_color = ('black','#F0F8FF')),
     sg.Button('÷', size = (7, 1.2), font=("ARIAL", 19), key = "-DIVIDED-", button_color = '#FFA500')],
    [sg.Button('7',size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('8', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('9', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('x', size = (7, 1.2), font=("ARIAL", 19), key = "-TIMES-", button_color = '#FFA500')],
    [sg.Button('4',size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('5', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('6', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('-', size = (7, 1.2), font=("ARIAL", 19),key = "-MINUS-",button_color = '#FFA500')],
    [sg.Button('1',size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('2', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('3', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button('+', size = (7, 1.2), font=("ARIAL", 19), key = "-PLUS-", button_color = '#FFA500')],
    [sg.Button('0',size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'),
     sg.Button(',', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'), 
     sg.Button('del', size = (7, 1.2), font=("ARIAL", 19), button_color = '#696969'), 
     sg.Button('=', size = (7, 1.2), font=("ARIAL", 19), button_color = '#FFA500')],

]

current_value = '0'
current_value_2 = ''
sign = ''
window = sg.Window('Калькулятор', layout, size=(600, 510), finalize=True, background_color = 'black')
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "AC":
        current_value = '0'
        window['-OUT_1-'].update(current_value)
        color_button(event)
        sign = ''
        current_value = '0'
        current_value_2 = ''

    elif event == "+/-":
        if current_value[0] == "-":
            current_value = current_value[1:]
        else:
            if current_value != '0':
                current_value =  '-' + current_value
        window['-OUT_1-'].update(current_value)


    elif event == "%":
        try:
            num = float(current_value) / 100
            current_value = str(num)
            window['-OUT_1-'].update(print_current_for_procent(num))
            print(print_current_for_procent(num))
        except ValueError:
            pass


    elif event == ",":
        if '.' not in current_value:
            current_value += "."
        else:
            continue
        window['-OUT_1-'].update(current_value)

    elif event == "-TIMES-":
        if sign == '':
            if current_value_2 == '':
                current_value_2 = current_value
                current_value = "0"
                color_button(event)
                sign = 'x'
        elif sign == 'x':
            pass
        else:
            sign = 'x'
            color_button(event)
    
    elif event == "-MINUS-":
        if sign == '':
            if current_value_2 == '':
                current_value_2 = current_value
                current_value = "0"
                color_button(event)
                sign = '-'
        elif sign == '-':
            pass
        else:
            sign = '-'
            color_button(event)

    elif event == "-PLUS-":
        if sign == '':
            if current_value_2 == '':
                current_value_2 = current_value
                current_value = "0"
                color_button(event)
                sign = '+'
        elif sign == '+':
            pass
        else:
            sign = '+'
            color_button(event)

    elif event == "-DIVIDED-":
        if sign == '':
            if current_value_2 == '':
                current_value_2 = current_value
                current_value = "0"
                color_button(event)
                sign = '÷'
        elif sign == '÷':
            pass
        else:
            sign = '÷'
            color_button(event)

    elif event == "=":
        if sign == '' or current_value == '0' or current_value_2 == '':
            continue
        else:
            equal(sign)
            sign = ''
            color_button(event)
    
    elif event == "del":
        if len(current_value) == 1:
            current_value = '0'
        else:
            current_value = current_value[:-1]
        window['-OUT_1-'].update(current_value)

    elif event in "0123456789":
        if current_value == '0':
            current_value = event
        else:
            current_value = current_value + event
        window['-OUT_1-'].update(current_value)



window.close()
exit(0)