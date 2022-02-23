from PyInstaller.__main__ import run
import pyautogui
import time
pyautogui.alert("O código será executado, por favor não mexa em nada até o final do processo")
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.PAUSE=10.0
pyautogui.hotkey('ctrl','t')#abre uma aba
time.sleep(2)
pyautogui.write('https://enterprise.leadlovers.com/leads')#escreve o link dos leads
pyautogui.press('enter')
time.sleep(10.0)
pyautogui.click(1320,171)# 3 pontos da página
pyautogui.PAUSE=2.0
pyautogui.click(1290,234)#botão de exportar
pyautogui.PAUSE=2.0
pyautogui.click(472,205)#primeira exportação
pyautogui.click(863,671)#botão de exportação
pyautogui.PAUSE=2.0
pyautogui.click(691,503)#botão de OK 
pyautogui.PAUSE=2.0
pyautogui.click(1320,171)# 3 pontos da página
pyautogui.PAUSE=2.0
pyautogui.click(1290,234)#botão de exportar
pyautogui.PAUSE=2.0
pyautogui.click(469,222)#segunda exportação
pyautogui.click(863,671)#botão de exportação
pyautogui.PAUSE=2.0
pyautogui.click(691,503)#botão de OK 
pyautogui.PAUSE=2.0
pyautogui.click(1320,171)# 3 pontos da página
pyautogui.PAUSE=2.0
pyautogui.click(1290,234)#botão de exportar
pyautogui.PAUSE=2.0
pyautogui.click(460,294)#terceria exportação
pyautogui.click(863,671)#botão de exportação
pyautogui.PAUSE=2.0
pyautogui.click(691,503)#botão de OK 
pyautogui.PAUSE=2.0
pyautogui.click(1320,171)# 3 pontos da página
pyautogui.PAUSE=2.0
pyautogui.click(1290,234)#botão de exportar
pyautogui.PAUSE=2.0
pyautogui.click(1320,171)#3 pontos
pyautogui.PAUSE=2.0
pyautogui.click(1290,234)#seção de exportar
pyautogui.click(565,430)
pyautogui.click(668,428)
pyautogui.click(772,428)
pyautogui.click(457,462)
pyautogui.click(562,461)
pyautogui.click(670,460)
pyautogui.click(773,460)
pyautogui.click(458,494)
pyautogui.click(564,490)
pyautogui.click(882,676)#botão de exportação final
pyautogui.click(754,413)#resgate de arquivos
pyautogui.alert("Exportações concluidas")
