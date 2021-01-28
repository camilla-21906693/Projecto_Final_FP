import teste

import pygame
import pygame.freetype

def menu():
    pygame.init()

    res = (1024, 768)

    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Wolf & Sheep Game")

    ovelha = pygame.image.load("ovelha.png")
    lobo = pygame.image.load("lobo.png")
    
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN:  
                if event.type == pygame.K_DOWN:
                    my_font.render_to(screen, (460,300), "PLAY", (255,0,0))
                    pygame.display.flip()


        screen.fill((0,0,20))
        my_font.render_to(screen, (300,20), "Welcome to Wolf and Sheep Game!", (64,224,208))
        my_font.render_to(screen, (460,300), "Play", (64,224,208))
        my_font.render_to(screen, (460,350), "Credits", (64,224,208))
        my_font.render_to(screen, (460,400), "Quit", (64,224,208))

        screen.blit(ovelha, (575, 325)) 
        screen.blit(lobo, (350,325))

        pygame.display.flip()

        
menu()