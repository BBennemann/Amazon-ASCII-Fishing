import random

import pygame

# INICIO
pygame.init()  # inicia o pygame
screen = pygame.display.set_mode((1000, 400))  # Configura a tela(Largura/Altura)
jogando = True

# ICONE E NOME
pygame.display.set_caption('Pescador')  # Nome da aba
icon = pygame.image.load('P.png')  # Importa a imagem de icone
pygame.display.set_icon(icon)  # Coloca o icone na janela

# IMAGEM FUNDO AMAZONIA
FundoC = pygame.image.load('FundoCompleto.png')  # Imagem Fundo da Amazonia
screen.blit(FundoC, (0, 0))  # Coloca a imagem na tela

# IMAGEM BARCO NORMAL
# BarcoN = pygame.image.load('Barco.png')  # Imagem barco

# IMAGEM BARCO LINHA
BarcoL = pygame.image.load('BarcoLinha.png')  # Imagem barco linha

# IMAGEM BARCO PEIXE
BarcoP = pygame.image.load('BarcoPeixe.png')  # Imagem barco peixe

# IMAGEM PESCAR
BotaoP = pygame.image.load('BotãoP2.png')  # Imagem botão pescar
#screen.blit(BotaoP, (840, 340))

# IMAGEM PEIXE PEGO
peixe_pego = pygame.image.load('PeixePego.png')  # Imagem peixe pego

clock = pygame.time.Clock()


def animacao_pesca():
    screen.blit(BarcoL, (0, 154))
    pygame.display.flip()
    pygame.time.wait(1000)
    screen.blit(BarcoP, (0, 154))
    pygame.display.flip()
    pygame.time.wait(1000)
    screen.blit(FundoC, (0, 0))
    pygame.display.flip()


def pesca_amazonia():
    Li = ['Lata', 'Bota']
    Co = ['Piranha', 'Jacunda', 'Oscar', 'Jatuarana', 'Curimatá', 'Tucunaré', 'Aruanã', 'Bicuda', 'Saicanga', 'Jaraqui']
    Ra = ['Poraquê', 'Tambaqui', 'Payara', 'Cachara', 'Pirarara', 'Trairão']
    Le = ['Pirarucu', 'Piraíba']
    Amazonia = (Co, Ra, Li, Ra, Co, Le, Co, Ra, Co, Co)
    x = random.randint(0, 9)
    y = random.randint(0, len(Amazonia[x]) - 1)
    return Amazonia[x][y]


font1 = pygame.font.SysFont('arial', 30)
text1 = font1.render(f'{"você pegou":^23}', True, (255, 255, 255))

while jogando:
    mouse = pygame.mouse.get_pos()
    clock.tick(60)  # FPS
    for event in pygame.event.get():  # pega os eventos
        if event.type == pygame.QUIT:  # Fecha o programa
            jogando = False
        if event.type == pygame.MOUSEBUTTONDOWN and 990 >= mouse[0] >= 840 and 389 >= mouse[1] >= 340:
            animacao_pesca()
            peixe = pesca_amazonia()
            screen.blit(peixe_pego, (350, 75))
            screen.blit(text1, (370, 73))
            text2 = font1.render(f'{f"um(a) {peixe}"}', True, (255, 255, 255))
            screen.blit(text2, (400, 100))
            pygame.display.flip()
            pygame.time.wait(1500)
            screen.blit(FundoC, (0, 0))
            pygame.display.flip()

    pygame.display.flip()  # Da update na tela
