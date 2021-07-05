#pip install pygame
from pandas.core.internals.managers import T
import pygame
#Incializar
pygame.init()
#Colores
negro = (0,0,0)
blanco = (255,255,255)
#Pantalla
pantalla_x = 800
pantalla_y = 600
tamanho_pantalla = (pantalla_x,pantalla_y)
#puntaje
puntaje_x = 200
puntaje_y = 100
cordenadas_x = pantalla_x//2 - (puntaje_x/2)
cordenadas_y = 0

puntaje_jugador_1 = 0
puntaje_jugador_2 = 0

font = pygame.font.Font('freesansbold.ttf', 22)
text_puntaje_1 = font.render(f'{puntaje_jugador_1}',True,(255,255,255),(0,0,0))
textRect_puntaje_1 = text_puntaje_1.get_rect()
textRect_puntaje_1.center = (cordenadas_x + (cordenadas_x/4), 50)

#Paleta
ancho_jugador = 15
alto_jugador = 90
#Creamos una pantalla
pantalla = pygame.display.set_mode(tamanho_pantalla)
#Reloj: FPS
reloj =pygame.time.Clock()
#Coordenadas de Jugador 1
jugador1_x = 50
jugador1_y = (pantalla_y//2) - (alto_jugador//2)
#Coordenadas de Jugador 2
jugador2_x = (pantalla_x-50)-ancho_jugador
jugador2_y = (pantalla_y//2) - (alto_jugador//2)
#Movimientos de los jugadores
mov_jugador1 = 0
mov_jugador2 = 0
#Coordenadas de la pelota
pelota_x = pantalla_x//2
pelota_y = pantalla_y//2
mov_pelota_x = 3
mov_pelota_y = 3
#Flag: bandera de fin de juego
game_over = False

partida_counter = 0
while not game_over:

    text_puntaje_2 = font.render(f'{puntaje_jugador_2}',True,(255,255,255),(0,0,0))
    textRect_puntaje_2 = text_puntaje_2.get_rect()
    textRect_puntaje_2.center = (cordenadas_x +((cordenadas_x/4)*2), 50)

    text_puntaje_1 = font.render(f'{puntaje_jugador_1}',True,(255,255,255),(0,0,0))
    textRect_puntaje_1 = text_puntaje_1.get_rect()
    textRect_puntaje_1.center = (cordenadas_x + (cordenadas_x/4) , 50) 
    # Gestionar eventos: detecta las acciones de los usuarios
    for evento in pygame.event.get():
        # print(evento)
        # Cuando presione X, debe salir
        if evento.type == pygame.QUIT:
            game_over = True
        #Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = -3
            if evento.key == pygame.K_s:
                mov_jugador1 = 3
            # Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = -3
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 3
        #Si se deja de presionar la tecla:
        if evento.type == pygame.KEYUP:
            # Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = 0
            if evento.key == pygame.K_s:
                mov_jugador1 = 0
            # Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = 0
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 0
    #Validación
    if pelota_y > pantalla_y or pelota_y < 0:
        mov_pelota_y *= -1
    #Si la pelota sale por el lado izquierdo o derecho es porque alguien perdió
    if pelota_x > pantalla_x:
        # La pelota se fue en esa -> direcion
        # punto para el jugador 1(izquierda)
        pelota_x = pantalla_x//2
        pelota_y = pantalla_y//2
        mov_pelota_x *= -1
        mov_pelota_y *= -1
        puntaje_jugador_1 += 1
        partida_counter += 1
        if partida_counter == 2 or partida_counter == 4 or partida_counter == 6 or partida_counter == 8:
            mov_pelota_y *= 1.2
            mov_pelota_x *= 1.2
        if puntaje_jugador_1 == 10: game_over = True
    if pelota_x<0:
        # <- esta direcion
        # punto para el jugador 2(derecha)
        pelota_x = pantalla_x//2
        pelota_y = pantalla_y//2
        mov_pelota_x *= -1
        mov_pelota_y *= -1
        puntaje_jugador_2 += 1
        partida_counter += 1
        if partida_counter == 2 or partida_counter == 4 or partida_counter == 6 or partida_counter == 8:
            mov_pelota_y *= 1.2
            mov_pelota_x *= 1.2
        if puntaje_jugador_2 == 10: game_over = True
    #Mover a los jugadores
    jugador1_y += mov_jugador1
    jugador2_y += mov_jugador2
    #Mover a la pelota
    pelota_x += mov_pelota_x
    pelota_y += mov_pelota_y
    #Gráficos
    pantalla.fill(negro)
    #Dibujamos Jugador 1
    jugador1 = pygame.draw.rect(pantalla, blanco, (jugador1_x, jugador1_y, ancho_jugador, alto_jugador))
    #Dibujamos Jugador 2
    jugador2 = pygame.draw.rect(pantalla, blanco, (jugador2_x, jugador2_y, ancho_jugador, alto_jugador))
    #Dibujamos la pelota
    pelota = pygame.draw.circle(pantalla, blanco, (pelota_x, pelota_y), 10)
    #Dibujamos el marcador
    marcador = pygame.draw.rect(pantalla, blanco, (cordenadas_x,cordenadas_y, puntaje_x,puntaje_y ))

    pantalla.blit(text_puntaje_1,textRect_puntaje_1)
    pantalla.blit(text_puntaje_2,textRect_puntaje_2)
    #Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        mov_pelota_x *=-1
    #Resfrescar pantalla
    pygame.display.flip()
    #FPS
    reloj.tick(60)

