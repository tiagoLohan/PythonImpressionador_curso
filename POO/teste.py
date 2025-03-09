import pyautogui
import pyperclip
import time

class Robo:

    def __init__(self, tempo_espera):
        self.tempo_espera = tempo_espera
        pyautogui.PAUSE = 1

    def abrir_programa(self, programa):
        pyautogui.press("win")
        pyautogui.write(programa)
        pyautogui.press("enter")

    def entrar_site(self, site):
        self._escrever_e_enter(site)
        self._aguardar()

    def _escrever_e_enter(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

    def _aguardar(self):
        time.sleep(self.tempo_espera)

    def pesquisa_no_campo(self, texto):
        self._escrever_e_enter(texto)
        self._aguardar()
        


robo1 = Robo(3)

robo1.abrir_programa("chrome")
robo1.entrar_site("www.hashtagtreinamentos.com.br")