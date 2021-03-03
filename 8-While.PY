# WHILE
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')

a = 1
while a < 60:
    lcd.escrever(board, 0, 0, 'CONTANDO             ')
    lcd.escrever(board, 0, 1, f'{a}                 ')
    a += 1
    if a == 49:
        break
time.sleep(100.0)
lcd.limpar(board)
board.exit()