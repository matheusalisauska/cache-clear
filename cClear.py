import PySimpleGUI as sg
import os
import time
import shutil

tempo = 5  # Tempo padrão de 5 segundos

def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Excluindo pasta: {folder_path}")
        print(f"Tempo para excluir: {tempo}")
    else:
        print("Essa pasta não existe!")
        print(f"Tempo para excluir: {tempo}")

def main():
    sg.theme('Dark')  # Mudar o tema para 'Dark'

    layout = [
        [sg.Text("Clear Cache:")],
        [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Text("Tempo para limpar (em segundos):"),
         sg.Input(key="-CLEAR_TIME-", default_text="5", size=(10, 1), enable_events=True, tooltip='Digite apenas números inteiros')],
        [sg.Button("Executar"), sg.Button("Parar"), sg.Button(key="-SET_TIME-", button_text="Definir tempo")]
    ]

    window = sg.Window("Cache Cleaner", layout)
    tempo = 5  # Tempo padrão de 5 segundos
    while True:
        event, values = window.read(timeout=tempo * 1000)  # Converter para milissegundos
    
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        elif event == "Executar":
            folder_path = values["-FOLDER-"]
            if folder_path:
                sg.popup(f"Você selecionou o diretório: {folder_path}")
                print(f"Diretório selecionado: {folder_path}")
            else:
                sg.popup("Nenhum diretório selecionado")
        elif event == "-SET_TIME-":
            try:
                tempo = int(values["-CLEAR_TIME-"])
                print(f"Tempo definido para {tempo}")
            except ValueError:
                sg.popup("Digite um número inteiro válido para o tempo de limpeza.")
                window["-CLEAR_TIME-"].update('')
        elif event == "__TIMEOUT__":
            folder_path = values["-FOLDER-"]
            if folder_path:
                delete_folder(folder_path)

        # Validação do input para aceitar somente números inteiros
        if event == "-CLEAR_TIME_INPUT-":
            input_value = values["-CLEAR_TIME_INPUT-"]
            if input_value and not input_value.isdigit():
                window["-CLEAR_TIME_INPUT-"].update('')

    window.close()

if __name__ == "__main__":
    main()
