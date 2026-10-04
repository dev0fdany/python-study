import pygame as p
from PIL import Image, ImageFilter

p.init()
screen = p.display.set_mode((1366,768))
clock = p.time.Clock()
test = p.image.load("face.png").convert_alpha()
test = p.transform.scale(test, (100,100))

bg = Image.open("/home/dwtop/Pictures/walls/ikuyo.png")
bg = bg.convert("RGB")
bg = bg.filter(ImageFilter.GaussianBlur(radius=2))
bg = p.image.fromstring(bg.tobytes(),bg.size,bg.mode)
#bg = p.image.load("/home/dwtop/Pictures/walls/ikuyo.png").convert()
bg = p.transform.smoothscale(bg, (1366,768))
imagex = 0 
speed = 10
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    imagex+= speed
    if imagex > 1466:
        imagex = -100
    screen.fill((50,50,50))
    screen.blit(bg, (0,0))
    screen.blit(test, (imagex,300))
    p.display.update()
    clock.tick(24)