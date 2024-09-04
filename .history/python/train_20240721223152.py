import pygame
# initializing imported module 
pygame.init() 
  
# displaying a window of height 
# 500 and width 400 
pygame.display.set_mode((500, 400)) 
  
# creating a bool value which checks 
# if game is running 
running = True
  
# keep game running till running is true 
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False