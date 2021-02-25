
# import pygame, time
# from pygame.locals import *
import csv
from time import sleep
from ctypes import windll, Structure, c_long, byref
# pygame.init()
# keys = pygame.key.get_pressed()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption('Pygame Keyboard Test')
# pygame.mouse.set_visible(0)

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [pt.x, pt.y]

filename = str(input('Vad vill du döpa filen till? '))

while True:
    sleep(0.01)
    with open (filename + '.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(queryMousePosition())
    # if keys[pygame.K_a]:
    #     print('break')
    #     break
