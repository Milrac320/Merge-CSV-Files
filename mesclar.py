import os
import csv
import openpyxl
import PySimpleGUI as sg

# Função para selecionar a pasta de origem
def selecionar_pasta_origem():
    global diretorio_origem
    diretorio_origem = sg.popup_get_folder("Selecione a Pasta de Origem")
    window['-ORIGEM-'].update(f'Pasta de Origem: {diretorio_origem}')

# Função para selecionar a pasta de destino
def selecionar_pasta_destino():
    global diretorio_destino
    diretorio_destino = sg.popup_get_folder("Selecione a Pasta de Destino")
    window['-DESTINO-'].update(f'Pasta de Destino: {diretorio_destino}')

# Função para mesclar arquivos CSV
def mesclar_csv():
    if not diretorio_origem or not diretorio_destino:
        sg.popup("Por favor, selecione as pastas faltantes!")
        return

    arquivos_csv = []

    # Itera sobre os arquivos no diretório de origem
    for arquivo in os.listdir(diretorio_origem):
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(diretorio_origem, arquivo)
            arquivos_csv.append(caminho_arquivo)

    # Cria um arquivo de saída mesclado
    saida_mesclada = []

    # Itera sobre os arquivos CSV e combina-os em "saida_mesclada"
    for arquivo_csv in arquivos_csv:
        with open(arquivo_csv, 'r', encoding='latin1') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for linha in csv_reader:
                saida_mesclada.append(linha)

    # Salva o resultado como um novo arquivo CSV na pasta de destino
    arquivo_saida = os.path.join(diretorio_destino, 'Arquivo_Mesclado.csv')
    with open(arquivo_saida, 'w', newline='', encoding='latin1') as csv_saida:
        csv_writer = csv.writer(csv_saida, delimiter=';')
        csv_writer.writerows(saida_mesclada)

sg.theme('DarkAmber')
layout = [
    [sg.Column([[sg.Button("Selecionar Pasta de Origem", key='-SELECT-ORIGEM-', size=(250))],
        [sg.Text("", key='-ORIGEM-')],
        [sg.Button("Selecionar Pasta de Destino", key='-SELECT-DESTINO-', size=(250))],
        [sg.Text("", key='-DESTINO-')],
        [sg.Button("Mesclar Arquivos", key='-MESCLAR-', size=(250))]], element_justification='c')],
]

window = sg.Window("Mesclar Arquivos CSV", layout, size=(700,180))

diretorio_origem = ""
diretorio_destino = ""

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == '-SELECT-ORIGEM-':
        selecionar_pasta_origem()
    elif event == '-SELECT-DESTINO-':
        selecionar_pasta_destino()
    elif event == '-MESCLAR-':
        mesclar_csv()

window.close()
