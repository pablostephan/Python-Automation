import pyautogui
import mouseinfo
import time

# Define uma pausa entre os comandos para evitar execução muito rápida
pyautogui.pause = 0.3

# Exibe informações da posição atual do mouse
print(pyautogui.mouseInfo())
time.sleep(5)

# Abre o navegador clicando no ícone da barra de tarefas
pyautogui.moveTo(1073,1048, duration=0.5)
pyautogui.click(1073,1048, duration=0.5)

# Digita o endereço do site na barra de navegação
pyautogui.moveTo(423,66, duration=0.5)
pyautogui.click(423,66, duration=0.5)
pyautogui.write('https://www.hashtagtreinamentos.com/')
pyautogui.press('enter')

# Aguarda o carregamento da página
time.sleep(5)

# Navega até a seção desejada do site
pyautogui.moveTo(468,193, duration=0.5)
pyautogui.moveTo(425,413, duration=0.5)
pyautogui.click(425,413, duration=0.5)
time.sleep(1)
pyautogui.scroll(-200)  # Rola a página para visualizar o formulário

# Preenche o formulário com nome, e-mail e telefone
pyautogui.moveTo(309,540, duration=0.5)
pyautogui.click(309,540, duration=0.5)
pyautogui.write('Pablo')
pyautogui.press('tab')
pyautogui.write('pablo.laffaet@gmail.com')
pyautogui.press('tab')
pyautogui.write('51995014566')
pyautogui.press('tab')
pyautogui.press('enter')  # Envia o formulário

# Aguarda carregar a página
time.sleep(8)
pyautogui.scroll(-200)