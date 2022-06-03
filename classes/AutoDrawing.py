import mouse
import keyboard
from PIL import Image
import random
import time

class AutoDrawing():
    def __init__(self, img, MousePos):
        self.img = img
        self.MousePos = MousePos
        self.width, self.height = self.img.size
        self.pix = self.img.load()
        self.point = []
        self.count = 0
        self.counter = 0
        
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.pix[i, j][0] <= 180 or self.pix[i, j][1] <= 180 or self.pix[i, j][2] <= 180:
                    self.point.append([i, j])
                    self.counter += 1

        random.shuffle(self.point)
        for i in self.point:
            mouse.move(self.MousePos[0] + i[0], self.MousePos[1] + i[1])
            mouse.click()
            self.count += 1
            if self.count % 10 == 0:
                time.sleep(0.01)
                self.count = 0
                print(self.counter)
