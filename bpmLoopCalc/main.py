import PySimpleGUI as sg
import time


def update(x, key):
    text_elem = window[key]
    text_elem.update("{}".format(x))


def conRound(x):
    if values["-check-"]:
        return round(x, 3)
    else:
        return round(x)


sg.theme('DarkAmber')
layout = [
    [sg.Text('BPM tool'), sg.Push(), sg.Checkbox('disable rounding', key='-check-')],
    [sg.Text('BPM:', size=(6, 1)), sg.InputText(size=(8, 1), key='-bpm-'), sg.Button('TAP BPM', size=(9, 1))],
    [sg.Text('Beats:', size=(6, 1)), sg.InputText(size=(8, 1), key='-aob-'), sg.Button('+1'), sg.Button('Reset')],
    [sg.Button('Calculate'), sg.Text("...", key='-calc-')]
]

# Create the Window
window = sg.Window('BPM TOOLS', layout)
T = []  # time difference
T1 = []  # time recorder

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    if event == 'Calculate':
        try:
            bpm = float(values['-bpm-'])
            aob = int(values['-aob-'])
            t = aob / (bpm / 60)
            update(str(round(t, 3)) + 's', '-calc-')
        except:
            update('err', '-calc-')

    if event == 'TAP BPM':
        T.append(time.monotonic())
        if len(T) > 1:
            dt = T[1] - T[0]
            T.pop(0)
            if dt > 3:
                T1 = []
            else:
                T1.append(conRound(60 / dt))
                bpm = sum(T1) / len(T1)
                update(conRound(bpm), '-bpm-')
    if event == 'Reset':
        update(0, '-aob-')
    if event == '+1':
        try:
            update(int(window['-aob-'].get()) + 1, '-aob-')
        except:
            update(1, '-aob-')

window.close()
