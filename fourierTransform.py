import sys
import pygame
import vectors
import math
import random
import fourierCalc
import path


pygame.init()

drawing = path.drawing
itera = len(drawing)//2
height = 900
width = 1500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
done = False
endpointsList = []
vectors_list = []

RED = pygame.Color("red")
BLUE = pygame.Color('blue')
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
GREY = pygame.Color(30,30,30)
font = pygame.font.Font('freesansbold.ttf', 50) 

a = 1                                                                                 
for i in range(itera):   
    ang = 180*fourierCalc.fourier(drawing, i)[1]/math.pi
    vector = vectors.vectors(a*i, ang)
    vectors_list.append(vector)
    if i != 0:
        ang = 180*fourierCalc.fourier(drawing, -1*i)[1]/math.pi
        vector = vectors.vectors(-1*a*i, ang)
        vectors_list.append(vector)
list_len = []
for i in range(itera*2-1):
    n = vectors_list[i].speed/a
    try:
        length = fourierCalc.fourier(drawing, n)[0]
    except:
        length = 0
    list_len.append(length)




while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
               
        
    for i in range(itera*2-1):
        
        n = vectors_list[i].speed/a
           
        try:
            num = list_len[i]   
        except ZeroDivisionError:
            num = 0
        if i == 0:
            vectors_list[i].update()
            vectors_list[i].ini(width//2, height//2, (num), 0, GREY, screen)
            vectors_list[i].rotate(screen, RED, GREY)
            
        else:
            vectors_list[i].update()
            vectors_list[i].ini(vectors_list[i-1].current_endpoint[0], vectors_list[i-1].current_endpoint[1],  num, 0, GREY, screen)
            vectors_list[i].rotate(screen, RED, GREY)

            
    endpointsList.append(vectors_list[-1].current_endpoint)
    for i in range(len(endpointsList)):
        try:
            pygame.draw.line(screen, WHITE, ((endpointsList[i][0], endpointsList[i][1])), ((endpointsList[i+1][0], endpointsList[i+1][1])))

            

        except Exception as e:
            pass
    if len(endpointsList) >= 360/a:
        endpointsList = []

    
    pygame.display.flip()
    clock.tick(0)

pygame.quit()
