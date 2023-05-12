import random
import sys
import pygame

pygame.init()

ANCHO = 800
ALTO = 600
rojo = (255, 0, 0)
negro = (0, 0, 0)
azul = (0, 0, 255)
blanco = (255, 255, 255)

jugador_size = 50
jugador_pos = [ANCHO / 2, ALTO - jugador_size*2]

enemigo_size = 50
enemigo_pos = [random.randint(0, ANCHO - enemigo_size), 0]

ventana = pygame.display.set_mode((ANCHO, ALTO))

game_over = False
clock = pygame.time.Clock()


pygame.display.set_caption("Mi Juego")


def draw_menu():
    title_font = pygame.font.SysFont(None, 60)
    title_text = title_font.render(
        "¡Bienvenido al Juego!", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(ANCHO/2, ALTO/4))

    menu_font = pygame.font.SysFont(None, 40)
    play_text = menu_font.render("Jugar", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(ANCHO/2, ALTO/2))

    quit_text = menu_font.render("Salir", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(
        center=(ANCHO/2, ALTO/2 + 50))

    ventana.blit(title_text, title_rect)
    ventana.blit(play_text, play_rect)
    ventana.blit(quit_text, quit_rect)


playing = False

while not playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # El jugador ha seleccionado "Jugar"
                playing = True
            elif event.key == pygame.K_ESCAPE:
                # El jugador ha seleccionado "Salir"
                sys.exit()
                playing = True

    draw_menu()

    pygame.display.update()

    def detectar_colision(jugador_pos, enemigo_pos):

        jx = jugador_pos[0]
        jy = jugador_pos[1]
        ex = enemigo_pos[0]
        ey = enemigo_pos[1]

        if (ex >= jx and ex < (jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)):
            if (ex >= jy and ey < (jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)):
                return True
        return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = jugador_pos[0]
            if event.key == pygame.K_LEFT:
                x -= jugador_size
            if event.key == pygame.K_RIGHT:
                x += jugador_size

            jugador_pos[0] = x

    ventana.fill(negro)

    if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
        enemigo_pos[1] += 20
    else:
        enemigo_pos[0] = random.randint(0, ANCHO - enemigo_size)
        enemigo_pos[1] = 0

    if detectar_colision(jugador_pos, enemigo_pos):
        game_over = True

    pygame.draw.rect(
        ventana, azul, (enemigo_pos[0], enemigo_pos[1], enemigo_size, enemigo_size))

    pygame.draw.rect(ventana, rojo,
                     (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
    clock.tick(30)
    pygame.display.update()
