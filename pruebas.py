import pygame
from fichas import *
from funciones import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode((450, 900))  #pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
tablero = tablero()
for i in range(0,15,1):
    tablero = unos(tablero,30,i)
gen = generar(120,-30)
piece =  gen.randomPieza()
color = gen.colores.get(piece)
actual = gen.generaPiece(piece,color)
rotacion = 0
lista = actual.dibujar(rotacion)
listaO =[]
FALL = pygame.USEREVENT + 1
pygame.time.set_timer(FALL, 200)

for objeto in lista: # se cambio el agregar la lista completa a listaO
    listaO.append(objeto)
key_state = False
m =0
print(len(listaO)/4)
while running:
    
     
    
    # Falta organizar la verificacion de la rotacion que no se salga de la pantalla

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    fichaList = posTabl(lista)
    coll = collis(tablero, fichaList)  # devuelve una lista con tuplas de coordenadas
    velocidad = veloc.get(actual.pieza)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                var = lista[:]
                siguiente = ladosPieza(var,actual,rotacion,1)


                if siguiente == True:

                    rotacion+=1
                        
                    if rotacion>3:
                        rotacion = 0
                        
                    fichaList = posTabl(lista)
                    minX = minValues(fichaList,'tup',0)
                    minY = minValues(fichaList,'tup',1)
                    lista = actual.rotar(rotacion,lista,minX,minY)
            
            elif event.key == pygame.K_z:
                var = lista[:]
                anterior = ladosPieza(var,actual,rotacion,-1)
                if anterior== True:

                    rotacion-= 1
                    if rotacion<0:
                        rotacion = 3
                
                    fichaList = posTabl(var)
                    minX = minValues(fichaList, 'tup', 0)
                    minY = minValues(fichaList, 'tup', 1)
                    lista = actual.rotar(rotacion,lista,minX,minY)


            elif event.key == pygame.K_LEFT:

                valcol = []
                valuesFich = []
                band = False
                cont = 0

                for tupla in fichaList:
                    valuesFich.append((tupla[0] - 30, tupla[1]))

                for tupla in coll:

                    if tupla[0] != -1:
                        valcol.append((tupla[0] * 30, tupla[1] * 30))

                for tuple in valuesFich:

                    if tuple in valcol or tuple[0] < 0:

                        band = True

                    else:

                        band = False
                        cont+=1

                if band == False and cont == 4:
                    lista[0].x -= 30
                    lista[1].x -= 30
                    lista[2].x -= 30
                    lista[3].x -= 30

            elif event.key == pygame.K_RIGHT:

                valcol = []
                valuesFich = []
                band = False
                cont = 0

                for tupla in fichaList:
                    valuesFich.append((tupla[0] + 30, tupla[1]))

                for tupla in coll:

                    if tupla[0] != -1:
                        valcol.append((tupla[0] * 30, tupla[1] * 30))

                for tuple in valuesFich:

                    if tuple in valcol or tuple[0] == 450:

                        band = True

                    else:

                        band = False
                        cont += 1

                if band == False and cont == 4:

                    lista[0].x += 30
                    lista[1].x += 30
                    lista[2].x += 30
                    lista[3].x += 30


                # fill the screen with a color to wipe away anything from last frame
            elif event.key == pygame.K_DOWN:

                valcol = []
                valuesFich = []
                band = False

                for tupla in fichaList:
                    valuesFich.append((tupla[0], tupla[1] + 30))

                for tupla in coll:

                    if tupla[0] != -1:
                        valcol.append((tupla[0] * 30, tupla[1] * 30))

                for tuple in valuesFich:

                    if tuple not in valcol:

                        band = True

                    else:

                        band = False

                if band:

                    lista[0].y += 30
                    lista[1].y += 30
                    lista[2].y += 30
                    lista[3].y += 30

        elif event.type == FALL:

            valcol = []
            valuesFich = []
            band = False


            for tupla in fichaList:

                valuesFich.append(( tupla[0] , tupla[1]+30 ))

            for tupla in coll:

                if tupla[0] != -1:

                    valcol.append(( tupla[0] * 30 , tupla[1] * 30 ))

            for tuple in valuesFich:

                    if tuple in valcol:

                        for x, y in fichaList:
                            i = int(x / 30)
                            j = int(y / 30)
                            tablero = unos(tablero, j, i)

                        nums = verificarUnos(tablero)
                        if len(nums) != 0:

                             listaO = eliminarUnos(listaO, nums)
                             tablero = actualizarTablero(tablero, nums)
                             listaO = bajarObj(nums, listaO)
                             tablero = bajarUnos(listaO)


                        piece = gen.randomPieza()
                        color = gen.colores.get(piece)
                        actual = gen.generaPiece(piece, color)
                        lista = []
                        lista = actual.dibujar(rotacion)

                        for objeto in lista:
                            listaO.append(objeto)

                        valcol = {}
                        valuesFich = {}


                        imprimirTablero(tablero)

                        break

                    else:

                        bajar = True
                        band = True

            if band:

                lista[0].y += 30
                lista[1].y += 30
                lista[2].y += 30
                lista[3].y += 30

    screen.fill((49,38,75))

    for coor in listaO: # for coor in objeto:
        pygame.draw.rect(screen,coor.color,[coor.x,coor.y,30,30])

    for i in range (0,450,30):
        rellenar(screen,(i,0),(i,900))
    for i in range(0,900,30):
        rellenar(screen,(0,i),(450,i))


    if 1 in tablero[3]:
        listaO.clear()

        piece =  gen.randomPieza()
        color =  gen.colores.get(piece)
        actual = gen.generaPiece(piece,color)
        lista = []
        lista = actual.dibujar(rotacion)
        for objeto in lista:
            listaO.append(objeto)

        imprimirTablero(tablero)
        for i in range(0,15,1):
            for j in range(0,30,1):
                tablero[j][i]=0
        for i in range(0,15,1):
            tablero = unos(tablero,30,i)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)/1000
    
    
pygame.quit()