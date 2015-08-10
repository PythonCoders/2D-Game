#Treasure Hunt - Part Two # A7 #
#Importing Libraries 
import pygame, random, sys, time, math, pygame.font, pygame.event, pygame.draw, time
import sys
import easygui
from math import sqrt,pow
#from Tkinter import *
#from tkMessageBox import *

#Initialise Pygame/canvas
pygame.init() #Initialise pygame
pygame.display.set_caption('Treasure Hunt') # Set the Title of window
screen = pygame.display.set_mode([640,480]) #Set the screen size

bg = pygame.image.load("background.jpg").convert() #Import background
background_position = [0,0] # Setting the position of the background
cfont = pygame.font.SysFont("Calibri", 24) #Set Font

white = (255,255,255) #Creating Colour white
black = (0,0,0) #Creating colour black
global_score = 0
items = []
shortlist = []
tcount = [0, 0, 0]
tvalue = [10, 20, 30]
timer_value = 5 #time limit of the round
time_reference = timer_value

#Creating Class for the Robot
class Robot:
    tR = [] #Robot list
    def __init__(self, x, y): #Initialise class
        self.x = x
        self.y = y
        self.ri = "robot.png"
        
    def create(self): #Create function
        self.rbti = pygame.image.load(self.ri)
        self.rect = self.rbti.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Robot.tR.append((self.rbti, self.rect))
        
    def rob_update(self): #Function used to update screen
        screen.blit(self.rbti, self.rect)
        
    def position(self): #Returns the position
        return self.rect
    
    def drag(self, x, y): #Drag and drop function
        self.old_loc = self.rect
        self.rect.x = x
        self.rect.y = y
        for i in range(len(Robot.tR)):
            if Robot.tR[i][1] == self.old_loc:
                Robot.tR[i] = (self.rbti, self.rect)
                
    def move(self,x,y): #Move function for the robot
        self.rect = self.rect.move(x,y)
        self.rob_update()


#Treasure Parent Class
class Treasure:
    def __init__(self, x, y):
        self.x= x
        self.y= y
#Sub classes of Treasure
class Treasure1(Treasure):
    tC = []
    def __init__(self, x, y):
        Treasure.__init__(self, x, y) # Inheriting x,y attribute from parent class
        self.ci = "treasure.png"
        self.gray = "gray.png"
    def create(self):
        self.cri = pygame.image.load(self.ci) #Loading image
        self.rect = self.cri.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Treasure1.tC.append((self.cri, self.rect))

    def remove(self):
        self.cri = pygame.image.load(self.gray) #Loading image
        self.rect = self.cri.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Treasure1.tC.append((self.cri, self.rect))


class Treasure2(Treasure):
    tC2 = []
    def __init__(self, x, y): 
        Treasure.__init__(self, x, y) # Inheriting x,y attribute from parent class
        self.bi = "treasure2.png"
        self.gray = "gray.png"
    def create(self):
        self.bri = pygame.image.load(self.bi) #Loading image
        self.rect = self.bri.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Treasure2.tC2.append((self.bri, self.rect))
    def remove(self):
        self.cri = pygame.image.load(self.gray) #Loading image
        self.rect = self.cri.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Treasure2.tC2.append((self.cri, self.rect))

class Treasure3(Treasure):
    tC3 = []
    def __init__(self, x, y):
        Treasure.__init__(self, x, y)# Inheriting x,y attribute from parent class
        self.bi2 = "treasure3.png"
        self.gray = "gray.png"
    def create(self):
        self.bri2 = pygame.image.load(self.bi2) #Loading image
        self.rect = self.bri2.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Treasure3.tC3.append((self.bri2, self.rect))
    def remove(self):
        self.cri = pygame.image.load(self.gray) #Loading image
        self.rect = self.cri.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        Treasure3.tC3.append((self.cri, self.rect))

def shortest(xcord, ycord, array):
    for i in range(0, len(array)):
#    print i
        diff1=botx-array[i][0]
      #  print array[0][1]
     #   print diff1
        diff2=boty-array[i][1]
        dist= sqrt(((pow((diff1),2))+(pow((diff2),2))))
      #  print dist
        if i == 0:
            short_dist = dist
            index = i
            short_array = array[i]

        if dist<short_dist:
            short_dist = dist
            index = i
            short_array = array[i]

    return [short_array, index]


#Update function
def update(): #Background updates
    screen.blit(bg, background_position) #Updating background
    pygame.font.SysFont("Calibri", 24) # Setting the font 
    screen.blit(cfont.render("Treasure:", 1, white),[10,40]) #Treasure text 
    screen.blit(cfont.render("Score:" + str(global_score), 1, white),[10,10]) #Score text
    screen.blit(cfont.render("Timer:" + str(timer_value), 1, white), [10,70]) #Timer text
    R1.rob_update() #Blitting the robot to screen
    pygame.display.flip()

def update2():  #Treasure Update
    for c in Treasure1.tC: #Treasure type 1 updates
        screen.blit(c[0], c[1])
    for b in Treasure2.tC2: #Treasure type 2 updates
        screen.blit(b[0], b[1])
    for a in Treasure3.tC3: #Treasure type 3 updates
        screen.blit(a[0], a[1])
    pygame.display.flip()

#Instance of Robot
R1=Robot(100,100) #Create robot
R1.create()
robots = [R1]

