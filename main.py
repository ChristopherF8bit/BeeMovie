import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionString, end='')
        print('\b' * len(positionString), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

def bee():
    time.sleep(5)
    pyautogui.position(x,y)
    pyautogui.click(x,y)
    file = open('BeeMovieScript.txt', 'r')
    try:
        for line in file:
            for char in line:
                pyautogui.typewrite(char)
    except KeyboardInterrupt:
        print('Bee Stoped')

explore = input(':')

if explore == 'bee':
    bee()
