import pygame

pygame.init()
tela  = pygame.display.set_mode((1200,700))
titulo= pygame.display.set_caption('RETANGULO MOVIMENTADO')
clock = pygame.time.Clock()

running =  True 
BLUE = 0,0,255
WHITE = "#FFFFFF"
X = 600
Y = 350
CIRCLE_X = 450
CIRCLE_y  = 300

radius = 30
TAMANHO = 50


while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running == False
        tela.fill(WHITE)

         # capturar os eventos do teclado: 
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
           X += 10
        elif teclas[pygame.K_LEFT]:
           X -= 50
        elif teclas[pygame.K_UP]:
           Y -= 2
        elif teclas[pygame.K_DOWN]:
           Y += 2    

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_d]:
           CIRCLE_X += 10
        elif teclas[pygame.K_a]:
           CIRCLE_X -= 50
        elif teclas[pygame.K_w]:
           CIRCLE_y -= 2
        elif teclas[pygame.K_s]:
           CIRCLE_y += 2                      

       
        pygame.draw.rect(tela, BLUE,(X,Y, TAMANHO, TAMANHO))
        pygame.draw.circle(tela, BLUE,(CIRCLE_X,CIRCLE_y),TAMANHO)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

pygame.quit()


