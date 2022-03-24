import pygame
#from pygame import event

screen=pygame.display.set_mode([640,480])

















x = 100
while True:

    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            quit()
            print(event)

    x+=1/10

    screen.fill([255,255,0])

    pygame.draw.circle(screen,[10,29,59],[x,240],45)
    pygame.display.flip()

