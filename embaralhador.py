import os, sys
from random import randint
from typing import overload
import pygame
import time

largura = 817
altura = 660
running = True
delay = 0.2
textScramble = []

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

movementValues = ['R', 'L', 'U', 'D', 'F', 'B']
valoresSecundarios = ["'", '²', '']
randomMovimentos = randint(0, 5)
redFace = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]

blueFace = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]

yellowFace = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]

whiteFace = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]

orangeFace = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]

greenFace = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']] 

gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)

pygame.init()
pygame.display.set_caption("Embaralhador Cubo Mágico")

screen = pygame.display.set_mode([largura, altura])
screen.fill((46, 46, 46))

def letterColor (letterColor):
    if letterColor == 'r':
        r = 183
        g = 18
        b = 52
    
    elif letterColor == 'b':
        r = 0
        g = 70
        b = 173

    elif letterColor == 'y':
        r = 255
        g = 213
        b = 0

    elif letterColor == 'w':
        r = 255
        g = 255
        b = 255
     
    elif letterColor == 'o':
        r = 255
        g = 88
        b = 0
    
    elif letterColor == 'g':
        r = 0
        g = 155
        b = 72
    return r, g, b

def showCube (cube):
    faceValue = 198
    posicoes = [[1*faceValue + 10, 0*faceValue + 5], [0*faceValue + 5, 1*faceValue + 10], [1*faceValue + 10, 1*faceValue + 10], [2*faceValue + 15, 1*faceValue + 10], [3*faceValue + 20, 1*faceValue + 10], [1*faceValue + 10, 2*faceValue +15]]
    #pygame.draw.line(screen, (0, 0, 0), (posicoes[0][0], posicoes[0][1] - 5), (posicoes[0][0] + faceValue, posicoes[0][1] - 5),  2)
    for face in range (6):
        for coluna in range (3):
            for linha in range (3):
                color = letterColor(cube[face][coluna][linha])
                pygame.draw.rect(screen, color, (posicoes[face][0], posicoes[face][1], faceValue/3, faceValue/3))
                posicoes[face][0] += faceValue/3
            posicoes[face][1] += faceValue/3
            posicoes[face][0] -= faceValue

def inverterBlue():
    tempMatriz = [['','',''],['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = blueFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            blueFace[x][y] = tempMatriz.copy()[x][y]

def r ():
    temp = ['','','']
    for x in range(3):
        temp [x] = greenFace.copy()[x][2]
        greenFace[x][2] = yellowFace.copy()[x][2]
        yellowFace[x][2] = blueFace.copy()[x][2]
        blueFace[x][2] = whiteFace.copy()[x][2]
        whiteFace[x][2] = temp.copy()[x]
    
    tempMatriz = [['','',''],['','',''], ['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = redFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            redFace[x][y] = tempMatriz.copy()[x][y]

def r2 ():
    r ()
    r ()

def rPrime ():
    temp = [[],[],[]]
    for x in range(3):
        temp [x] = greenFace.copy()[x][2]
        greenFace[x][2] = whiteFace.copy()[x][2]
        whiteFace[x][2] = blueFace.copy()[x][2]
        blueFace[x][2] = yellowFace.copy()[x][2]
        yellowFace[x][2] = temp.copy()[x]
    
    tempMatriz = [['','',''], ['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[2-y][x] = redFace.copy()[x][y]

    for x in range (3):
        for y in range (3):
            redFace[x][y] = tempMatriz.copy()[x][y]
    
def l ():
    temp = [[],[],[]]
    for x in range(3):
        temp [x] = greenFace.copy()[x][0]
        greenFace[x][0] = whiteFace.copy()[x][0]
        whiteFace[x][0] = blueFace.copy()[x][0]
        blueFace[x][0] = yellowFace.copy()[x][0]
        yellowFace[x][0] = temp.copy()[x]

    tempMatriz = [['','',''],['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = orangeFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            orangeFace[x][y] = tempMatriz.copy()[x][y]

def l2 ():
    l ()
    l ()

def lPrime ():
    temp = [[],[],[]]
    for x in range(3):
        temp [x] = greenFace.copy()[x][0]
        greenFace[x][0] = yellowFace.copy()[x][0]
        yellowFace[x][0] = blueFace.copy()[x][0]
        blueFace[x][0] = whiteFace.copy()[x][0]
        whiteFace[x][0] = temp.copy()[x]
    
    tempMatriz = [['','',''], ['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[2-y][x] = orangeFace.copy()[x][y]

    for x in range (3):
        for y in range (3):
            orangeFace[x][y] = tempMatriz.copy()[x][y]

def u():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = greenFace.copy()[0][x]
        greenFace[0][x] = redFace.copy()[0][x]
        redFace[0][x] = blueFace.copy()[2][2-x]
        blueFace[2][2-x] = orangeFace.copy()[0][x]
        orangeFace[0][x] = temp[x]

    tempMatriz = [['','',''],['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = whiteFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            whiteFace[x][y] = tempMatriz.copy()[x][y]

def u2():
    u()
    u()

def uPrime():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = greenFace.copy()[0][x]
        greenFace[0][x] = orangeFace.copy()[0][x]
        orangeFace[0][x] = blueFace.copy()[2][2-x]
        blueFace[2][2-x] = redFace.copy()[0][x]
        redFace[0][x] = temp[x]

    tempMatriz = [['','',''], ['','',''], ['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[2-y][x] = whiteFace.copy()[x][y]

    for x in range (3):
        for y in range (3):
            whiteFace[x][y] = tempMatriz.copy()[x][y]

def d():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = greenFace.copy()[2][x]
        greenFace[2][x] = orangeFace.copy()[2][x]
        orangeFace[2][x] = blueFace.copy()[0][2-x]
        blueFace[0][2-x] = redFace.copy()[2][x]
        redFace[2][x] = temp[x]

    tempMatriz = [['','',''],['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = yellowFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            yellowFace[x][y] = tempMatriz.copy()[x][y]

def d2():
    d()
    d()

def dPrime():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = greenFace.copy()[2][x]
        greenFace[2][x] = redFace.copy()[2][x]
        redFace[2][x] = blueFace.copy()[0][2-x]
        blueFace[0][2-x] = orangeFace.copy()[2][x]
        orangeFace[2][x] = temp[x]
    
    tempMatriz = [['','',''], ['','',''], ['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[2-y][x] = yellowFace.copy()[x][y]

    for x in range (3):
        for y in range (3):
            yellowFace[x][y] = tempMatriz.copy()[x][y]

def f():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = whiteFace.copy()[2][x]
        whiteFace[2][x] = orangeFace.copy()[2-x][2]
        orangeFace[2-x][2] = yellowFace.copy()[0][2-x]
        yellowFace[0][2-x] = redFace.copy()[x][0]
        redFace[x][0] = temp[x]

    tempMatriz = [['','',''],['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = greenFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            greenFace[x][y] = tempMatriz.copy()[x][y]
        
def f2 ():
    f()
    f()

def fPrime():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = whiteFace.copy()[2][x]
        whiteFace[2][x] = redFace.copy()[x][0]
        redFace[x][0] = yellowFace.copy()[0][2-x]
        yellowFace[0][2-x] = orangeFace.copy()[2-x][2]
        orangeFace[2-x][2] = temp[x]

    tempMatriz = [['','',''], ['','',''], ['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[2-y][x] = greenFace.copy()[x][y]

    for x in range (3):
        for y in range (3):
            greenFace[x][y] = tempMatriz.copy()[x][y]

def b():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = whiteFace.copy()[0][x]
        whiteFace[0][x] = redFace.copy()[x][2]
        redFace[x][2] = yellowFace.copy()[2][2-x]
        yellowFace[2][2-x] = orangeFace.copy()[2-x][0]
        orangeFace[2-x][0] = temp[x]
    
    tempMatriz = [['','',''],['','',''],['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[x][2-y] = blueFace.copy()[y][x]
    for x in range (3):
        for y in range (3):
            blueFace[x][y] = tempMatriz.copy()[x][y]

def b2():
    b()
    b()

def bPrime():
    temp = [[],[],[]]
    for x in range (3):
        temp [x] = whiteFace.copy()[0][x]
        whiteFace[0][x] = orangeFace.copy()[2-x][0]
        orangeFace[2-x][0] = yellowFace.copy()[2][2-x]
        yellowFace[2][2-x] = redFace.copy()[x][2]
        redFace[x][2] = temp[x]
    
    tempMatriz = [['','',''], ['','',''], ['','','']]
    for y in range (3):
        for x in range (3):
            tempMatriz[2-y][x] = blueFace.copy()[x][y]

    for x in range (3):
        for y in range (3):
            blueFace[x][y] = tempMatriz.copy()[x][y]

def identifyMove (move):
    if move == "R":
        r()

    elif move == "R²":
        r2()

    elif move == "R'":
        rPrime()

    elif move == "L":
        l()

    elif move == "L²":
        l2()
        
    elif move == "L'":
        lPrime()
    
    elif move == "U":
        u()

    elif move == "U²":
        u2()
        
    elif move == "U'":
        uPrime()

    elif move == "D":
        d()

    elif move == "D²":
        d2()
        
    elif move == "D'":
        dPrime()

    elif move == "F":
        f()

    elif move == "F²":
        f2()
        
    elif move == "F'":
        fPrime()
    
    elif move == "B":
        b()

    elif move == "B²":
        b2()
        
    elif move == "B'":
        bPrime()
    
for x in range(19):
    novoRandomMovimentos = randint(0, 5)
    while True:
        if novoRandomMovimentos == randomMovimentos:
            novoRandomMovimentos = randint(0, 5)
        else:
            randomMovimentos = novoRandomMovimentos
            break   
        
    randomSecundarios = randint(0, 2)
    tempMove = movementValues[randomMovimentos] + valoresSecundarios[randomSecundarios]
    textScramble.append(tempMove)
    identifyMove(tempMove)

    if x == 18:
        inverterBlue()
        inverterBlue()
    
    cube = [whiteFace, orangeFace, greenFace, redFace, blueFace, yellowFace] 
    time.sleep(delay)
    pygame.display.flip()
    showCube(cube)

for movimento in textScramble:
    print(f"{movimento}", end = ' ')

print()
print()

print("GREEN")
print("="*30)
for x in range (3):
    for y in range (3):
        print(greenFace[x][y], end = ' ')
    print()

print()

print("RED")
print("="*30)
for x in range (3):
    for y in range (3):
        print(redFace[x][y], end = ' ')
    print()

print()

print("BLUE")
print("="*30)
for x in range (3):
    for y in range (3):
        print(blueFace[x][y], end = ' ')
    print()

print()

print("ORANGE")
print("="*30)
for x in range (3):
    for y in range (3):
        print(orangeFace[x][y], end = ' ')
    print()

print()

print("WHITE")
print("="*30)
for x in range (3):
    for y in range (3):
        print(whiteFace[x][y], end = ' ')
    print()

print()

print("YELLOW")
print("="*30)
for x in range (3):
    for y in range (3):
        print(yellowFace[x][y], end = ' ')
    print()

while running:

    #Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    txt = ''
    for movimento in textScramble:
        txt += f"{movimento}   "

    #pygame.font.init()
    #fonte = pygame.font.get_default_font()
    #fontesys = pygame.font.SysFont(fonte, 33)
    #txttela = fontesys.render(txt, 1, (255,255,255))
    #screen.blit(txttela,(10,615))
    
    font = pygame.font.Font(None, 33)
    text = font.render(txt, True, (255, 255, 255))
    text_rect = text.get_rect(center=(largura/2, 635))
    screen.blit(text, text_rect)
    
    pygame.display.flip()

pygame.quit()