from classes.MainWindow import MainWindow
import threading
import keyboard
import os

def stop():
    keyboard.wait(hotkey = "ctrl + z")
    os._exit(0)

threadingObj = threading.Thread(target= stop, daemon= True)
threadingObj.start()
mw = MainWindow()
mw.start()