import os
import time
import pyautogui
import subprocess

clear = lambda: os.system('cls') #on Windows System

print('GUISUP')
print('Type "help" to help')
print(' ')

for i in range(1881):
    pyautogui.FAILSAFE = False
    giris = input('GUISUP>>>  ')

    if 'http' in giris:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write(giris)
        pyautogui.press('enter')
    elif 'www' in giris:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write(giris)
        pyautogui.press('enter')
    elif '.com' in giris:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write(giris)
        pyautogui.press('enter')
    elif 'yt' in giris:
        pyautogui.hotkey('win', 'r')
        pyautogui.write(giris)
        pyautogui.press('home')
        pyautogui.press('del', presses=3)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('https://www.youtube.com')
        time.sleep(0.10)
        pyautogui.press('backspace')
        time.sleep(0.10)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('tab', presses=4, interval=0.25) #buradan sonrasi yt aramasi
        time.sleep(0.25)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.25)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('tab')
        time.sleep(0.25)
        pyautogui.press('enter')
    elif 'youtube' in giris:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('https://www.youtube.com')
        pyautogui.press('enter')
    elif 'wp' in giris:
        #subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('https://web.whatsapp.com/')
        pyautogui.press('enter')
    elif 'help' in giris:
        clear()
        print('    Only paste your link to search in Chrome')
        print('    Type "youtube" to go')
        print('    To watch on Youtube: "yt (video name)"')
        print('    Type "wp" to open Whatsapp Web')
        print('    If you want to run installed app, just write its name (you can write short name)')
        print('    If you want to browse on web, just type what do you want')
        print('    "clear" to clear')
        print(' ')
        print('Author => github: umutkcbs    /    gmail: ugorkemkocabas@gmail.com')
        print(' ')
    elif 'clear' in giris:
        clear()
    else:
        pyautogui.press('win')
        pyautogui.write(giris)
        pyautogui.press('enter')