
import sys
# # you will need to change the path to your sigverse workspace directory
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/pygame/')

import time
import threading


import pygame
from pygame.locals import *

# pos=[]



def on_mouseMotionNew():

    background_colour = (255,255,255)
    screen = pygame.display.set_mode((620, 400))
    screen.fill(background_colour)
    flag=0
    running=1
    num=[]
    pos=[]
    posAbs=[]
    posRel=[]
    # global pos

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            (a,b,c)= pygame.mouse.get_pressed()
            if a == 1:
                print "the left button is pressed, logging starts"
                    # print "mouse at (%d, %d)" % event.pos
                flag=1           
            
            elif c==1:
                print "the right button is pressed, logging stops"
                flag=0       

        if event.type == pygame.MOUSEMOTION and flag==1:
                # print "mouse at (%d, %d)" % event.pos
            # pos=list(event.pos)
            pos=list(pygame.mouse.get_rel())
            # print pos
                # print "relative pos is (%d, %d)" % pygame.mouse.get_rel()
            # num.append(pos)
            pygame.draw.circle(screen, (0,0,240),event.pos, 3,1)
            pygame.display.flip()
            yield pos



    pygame.quit()
    # return pos
    # yield pos
    # return num



a=on_mouseMotionNew()


print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)

print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)

print next(a)
print next(a)
print next(a)
print next(a)



pygame.quit()

