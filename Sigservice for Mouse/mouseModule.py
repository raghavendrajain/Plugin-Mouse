import sys
import time
import threading
import pygame
from pygame.locals import *

pos=[]
 
class App:
    def __init__(self):
        self._running = True
     
    def on_init(self):
        # pygame.init()
        # self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        screen = pygame.display.set_mode((620, 400))
        self._running = True
        self.flag=0
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()

    def on_mouseMotionNew(self):
        background_colour = (255,255,255)
        screen = pygame.display.set_mode((620, 400))
        screen.fill(background_colour)
        flag=0
        running=1
        num=[]
        # pos=[]
        posAbs=[]
        posRel=[]
        global pos

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
                    count=0          
            
                elif c==1:
                    print "the right button is pressed, logging stops"
                    flag=0
                    flagList=[flag]
                    yield flagList      

            if event.type == pygame.MOUSEMOTION and flag==1:
                # print "mouse at (%d, %d)" % event.pos
                # pos=list(event.pos)
                count=count+1        
                pos=list(pygame.mouse.get_rel())
                # print "relative pos is (%d, %d)" % pygame.mouse.get_rel()
                # num.append(pos)
                pygame.draw.circle(screen, (0,0,240),event.pos, 3,1)
                pygame.display.flip()

                if count==1:
                    pass
                else:

                    yield pos

        pygame.quit()
        # return num

if __name__ == "__main__" :
    theApp = App()
    a=theApp.on_mouseMotionNew()
    for i in range(0,100):
        print next(a)
    pygame.quit()




