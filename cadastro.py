from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('Reddit')
tela = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# janela
janela = sg.Window('Tela de Login', tela)
# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Gabriel' and valores['senha'] == '123456':
            print('Seja bem vindo')
