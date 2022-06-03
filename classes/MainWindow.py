from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageGrab, ImageFilter
from classes.AutoDrawing import AutoDrawing
import keyboard
import pyautogui
import mouse
import json
import threading


class MainWindow():

    def __init__(self):
        with open("resource//base.json", 'r', encoding = 'utf-8') as jfile:
            self.jdata = json.load(fp = jfile)
        
        self.root = Tk()
        self.root.geometry("320x180")
        self.root.title("AutoDrawing")
        
        self.styleButton = ttk.Style(self.root)
        self.styleButton.configure('basic.TButton', font = self.jdata['font'])
        
        self.buttonSelect = ttk.Button(self.root, text = "選擇區域", style = 'basic.TButton', command = self.firstSelect)
        self.buttonReSelect = ttk.Button(self.root, text = "重新選擇區域", style = 'basic.TButton', command = self.reSelect)
        self.buttonStart = ttk.Button(self.root, text = "開始繪圖", style = 'basic.TButton', command = self.startDrawing)
        
        self.imglabel = ttk.Label()
        
        self.firstPlace()

    def firstPlace(self):
        self.buttonSelect.pack()

    def update(self):
        self.root.geometry(str(int(self.imgFilter.size[0] / 1.3) + 100) + "x" + str(int(self.imgFilter.size[1] / 1.3) + 100))
        self.imglabel.pack()
        self.buttonReSelect.pack()
        self.buttonStart.pack()
        self.root.state("normal")

    def firstSelect(self):
        self.root.state("icon")
        
        self.screenshot()
        self.buttonSelect.destroy()
        self.update()

    def reSelect(self):
        self.root.state("icon")
        
        self.screenshot()
        self.update()

    def screenshot(self):
        mouse.wait(button = "left", target_types = "down")
        self.x1, self.y1 = pyautogui.position()
        mouse.wait(button = "right", target_types = "down")
        self.x2, self.y2 = pyautogui.position()

        self.img = ImageGrab.grab(all_screens= True)
        self.imgCrop = self.img.crop((self.x1, self.y1, self.x2, self.y2))
        self.imgCrop.save("picture//screemshot.png")
        self.imgFilter = self.imgCrop.filter(ImageFilter.CONTOUR)
        self.imgFilter.save("picture//contour.png")
        self.imgResize = self.imgCrop.resize((int(self.imgCrop.size[0] / 1.3), int(self.imgCrop.size[1] / 1.3)))
        self.imgtk = ImageTk.PhotoImage(self.imgResize)
        self.imglabel.config(image = self.imgtk)

    def startDrawing(self):
        self.root.state("icon")
        keyboard.wait('ctrl')
        self.auto = AutoDrawing(self.imgFilter.resize((int(self.imgFilter.size[0] / 1.3), int(self.imgFilter.size[1] / 1.3))), pyautogui.position())
        self.root.state("normal")


    def start(self):
        self.root.mainloop()


        
        

        
        