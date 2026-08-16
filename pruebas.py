import pygame
from fichas import *

# pygame setup
pygame.init()
info = pygame.display.Info()
width = int((info.current_w)//3)
CENTRO = ((width/2)//30)*30
height = int((info.current_h)*0.8)

screen = pygame.display.set_mode((width, height))  #pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
tablero = tablero(int(width//30),int((height+30)//30))

for i in range(0,width//30,1):  # cambiado
    tablero = unos(tablero,int(len(tablero)-1),i) # cambiado

piece =  random.choice(formas)
color = colores[piece]
lista = bloques(matrices[piece],color,CENTRO,0)
actual = Pieza(int(((width//30)//3)*30),0,piece,lista)
rotacion = 0

listaO =[]
FALL = pygame.USEREVENT + 1
pygame.time.set_timer(FALL, 500)

#for objeto in lista: # se cambio el agregar la lista completa a listaO
    #listaO.append(objeto)

key_state = False
m =0
imprimirTablero(tablero)
while running:




    # Falta organizar la verificacion de la rotacion que no se salga de la pantalla

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                actual.rotar(width)

            elif event.key == pygame.K_z:
                pass

            elif event.key == pygame.K_LEFT and collis(actual,(-1,0),width,height,tablero):

                    actual.bloques[0].x -= 30
                    actual.bloques[1].x -= 30
                    actual.bloques[2].x -= 30
                    actual.bloques[3].x -= 30


            elif event.key == pygame.K_RIGHT and collis(actual,(1,0),width,height,tablero):

                    actual.bloques[0].x += 30
                    actual.bloques[1].x += 30
                    actual.bloques[2].x += 30
                    actual.bloques[3].x += 30


                # fill the screen with a color to wipe away anything from last frame

            elif event.key == pygame.K_DOWN and collisUnos(actual,(0,1),tablero):

                    actual.bloques[0].y += 30
                    actual.bloques[1].y += 30
                    actual.bloques[2].y += 30
                    actual.bloques[3].y += 30



        elif event.type == FALL :



            if collisUnos(actual, (0,1), tablero):  # verificar si hay ceros debajo

                actual.bloques[0].y += 30
                actual.bloques[1].y += 30
                actual.bloques[2].y += 30
                actual.bloques[3].y += 30

            else:

                lislin = []
                for bloque in lista:

                    tablero = unos(tablero,int(bloque.y//30),int(bloque.x//30)) # llenar unos de fichas
                    estado = verificarUnos(tablero,width,int(bloque.y//30))  # verificar si esta llena la linea

                    if estado:
                       lislin.append(int(bloque.y//30))

                if estado:
                       #tablero = actualizarTablero(tablero,int(bloque.y//30),width)  # borra 1 y llena 0
                    listaO = eliminarUnos(listaO,lislin)  # borrar objetos bloques
                    actual.bloques = eliminarUnos((actual.bloques), lislin)
                    actual.bloques = bajarObj(lislin, actual.bloques)
                    listaO = bajarObj(lislin,listaO)
                    tablero = bajarUnos(listaO,actual.bloques,width,height,tablero)
                for objeto in actual.bloques:  # se cambio el agregar la lista completa a listaO
                    listaO.append(objeto)
                lista = 0
                piece = random.choice(formas)
                color = colores[piece]
                lista = bloques(matrices[piece], color, CENTRO, 0)
                actual = Pieza(int(((width // 30) // 3) * 30), 0, piece, lista)
                imprimirTablero(tablero)
                print('---------------------------------------------------------')






    screen.fill((49,38,75))

    for bloque in actual.bloques:
        pygame.draw.rect(screen, bloque.color, [bloque.x, bloque.y, 30, 30])

    for coor in listaO: # for coor in objeto:
        pygame.draw.rect(screen,coor.color,[coor.x,coor.y,30,30])



    for i in range (0,int(width),30):
        rellenar(screen,(i,0),(i,height))
    for i in range(0,int(height),30):
        rellenar(screen,(0,i),(width,i))


    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.


pygame.quit()