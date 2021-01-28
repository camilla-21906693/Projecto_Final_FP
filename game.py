import pygame

PRETO = (0,0,0)
VERDE = (0,255,0)
VERMELHO = (255,0,0)

def tabuleiro_default(screen, ovelha, lobo):
    desenha = False

    i = 0
    coord = []
    verificador_ovelha = []
    verificador_lobo = []

    for i in range (8):
        verificador_ovelha.append([False,False,False,False,False,False,False,False])
        verificador_lobo.append([False,False,False,False,False,False,False,False])

    matriz_tabuleiro = [['-','x','-','x','-','x','-','x'],
						['-','-','-','-','-','-','-','-'],
				  		['-','-','-','-','-','-','-','-'],
						['-','-','-','-','-','-','-','-'],
						['-','-','-','-','-','-','-','-'],
						['-','-','-','-','-','-','-','-'],
						['-','-','-','-','-','-','-','-'],
						['-','-','-','-','o','-','-','-']]

    for i in range (8):
        for j in range(8):
            x = 220 + (j * 75)
            y = 100 + (i * 75)
            coord.append([x,y])
                        
    pieces = {'sheep' : ovelha, 'wolf' : lobo}

    for row in range(8):
        for rect in range(8):
            x = 220 + (rect * 75)
            y = 100 + (row * 75)
            pygame.draw.rect(screen, VERDE,( x, y, 75, 75), 1)
            
            if matriz_tabuleiro[row][rect] == 'x':
                screen.blit(pieces['wolf'], (x,y))
                verificador_lobo[row][rect] = True
            elif matriz_tabuleiro[row][rect] == 'o':
                screen.blit(pieces['sheep'], (x,y))
                verificador_ovelha[row][rect] = True
            
            i += 1
    
def main():
    desenha = False

    pygame.init()

    res = (1024, 768)
    ovelha = pygame.image.load("ovelha.png")
    lobo = pygame.image.load("lobo.png")

    screen = pygame.display.set_mode(res)
    # Nome da janela do programa
    pygame.display.set_caption("Wolf & Sheep Game")

    while True:
        mb = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()

            if (mb[0]):
                if 220 < pos[0] < 820 and 100 < pos[1] < 700:
                    xi = int((pos[0] - 220) / 75)
                    yi = int((pos[1] - 100) / 75)

                    for i in range(8):
                        for j in range(8):
                            x = 220 + (xi * 75)
                            y = 100 + (yi * 75)

                    desenha = True
       
        #desenhando o tabuleiro
        if desenha:
            pygame.draw.rect(screen, VERDE, (x, y, 75, 75))
        
        tabuleiro_default(screen, ovelha, lobo)
        pygame.display.flip()
        screen.fill((0,0,20))

main()