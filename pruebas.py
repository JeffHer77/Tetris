import pygame
from fichas import *
from funciones import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode((450, 900))  #pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
tablero = tablero()
for i in range(0,15,1):
    tablero = unos(tablero,30,i)
gen = generar(120,-30)
piece =  gen.randomPieza()
color = gen.colores.get('l')
ele = gen.generaPiece('l',color)
rotacion = 0
lista = ele.dibujar(rotacion)
actual = ele
listaO =[]
for objeto in lista: # se cambio el agregar la lista completa a listaO
    listaO.append(objeto)
key_state = False
m =0

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
                #print(siguiente)

                if siguiente == True:
                    print(2)
                    print('max x sg')
                    print(maxValues(var,'x'))
                    rotacion+=1
                        
                    if rotacion>3:
                        rotacion = 0
                        
                    fichaList = posTabl(lista)
                    minX = minValues(fichaList,'tup',0)
                    minY = minValues(fichaList,'tup',1)
                    lista = actual.rotar(rotacion,lista,minX,minY)
            
            elif event.key == pygame.K_z:
                var = lista[:]
                anterior = ladosPieza(lista,actual,rotacion,-1) 
                if anterior== True:
                    print(3)
                    print('max x an')
                    print(maxValues(var, 'x'))
                    rotacion-= 1
                    if rotacion<0:
                        rotacion = 3
                
                    fichaList = posTabl(lista)
                    minX = minValues(fichaList, 'tup', 0)
                    minY = minValues(fichaList, 'tup', 1)
                    lista = actual.rotar(rotacion,lista,minX,minY)


            elif event.key == pygame.K_LEFT:


                mins = []
                objX = []
                for tupla in coll:

                    mins.append(tupla[0])

                print("LEFT")
                print(fichaList)
                print(coll)
                print(mins)


                if (len(mins) > 1):
                    left = min(mins)
                else:
                    left = mins[0]

                for objeto in lista:

                    x1 = objeto.x
                    objX.append(x1)

                minObj = min(objX)

                if left != -1:
                    if (minObj >= left + 30 and minObj >= 0 + velocidad):
                        lista[0].x -= 30
                        lista[1].x -= 30
                        lista[2].x -= 30
                        lista[3].x -= 30

                        mins = []
                        objX =[]
                        minObj = 0
                else:
                    if minObj >= 30:
                        lista[0].x -= 30 # * dt
                        lista[1].x -= 30
                        lista[2].x -= 30
                        lista[3].x -= 30

                        mins = []
                        objX =[]
                        minObj = 0

            elif event.key == pygame.K_RIGHT:


                maxR= []
                objX = []

                for tupla in coll:

                    maxR.append(tupla[0])



                if (len(maxR) > 1):
                    right = max(maxR)

                else:
                    right = maxR[0]

                for objeto in lista:

                    x1 = objeto.x
                    objX.append(x1)

                maxObj = max(objX)

                print(fichaList)
                print(coll)
                print(maxR)

                if right != -1:
                    if (maxObj <= right - 30 and maxObj <= 420):
                        lista[0].x += 30
                        lista[1].x += 30
                        lista[2].x += 30
                        lista[3].x += 30

                else:
                    print(maxObj)
                    if maxObj <= 390:
                        lista[0].x += 30
                        lista[1].x += 30
                        lista[2].x += 30
                        lista[3].x += 30

                        # fill the screen with a color to wipe away anything from last frame
            elif event.key == pygame.K_DOWN:

                maxy = []
                objY = []

                for tupla in coll:

                    maxy.append(tupla[1])

                print("DOWN")
                print(fichaList)
                print(coll)
                print(maxy)

                if (len(maxy) > 1):
                    down = max(maxy)
                else:
                    down = maxy[0]

                for objeto in lista:
                    y1 = objeto.x
                    objY.append(y1)

                maxObj = max(objY)

                if down != -1:
                    if (maxObj <= down - 30 and maxObj <= 870):
                        lista[0].y += 30
                        lista[1].y += 30
                        lista[2].y += 30
                        lista[3].y += 30

                    else:


                        piece = gen.randomPieza()
                        color = gen.colores.get(piece)
                        actual = gen.generaPiece(piece, color)
                        lista = []
                        lista = actual.dibujar(rotacion)

                        for objeto in lista:
                            listaO.append(objeto)

                else:
                    if maxObj <= 870:
                        lista[0].y += 30
                        lista[1].y += 30
                        lista[2].y += 30
                        lista[3].y += 30

                    else:

                        piece = gen.randomPieza()
                        color = gen.colores.get(piece)
                        actual = gen.generaPiece(piece, color)
                        lista = []
                        lista = actual.dibujar(rotacion)

                        for objeto in lista:
                            listaO.append(objeto)


    screen.fill((49,38,75))

    #for coor in lista:
        #pygame.draw.rect(screen,color,[coor.x,coor.y,30,30])

    #for objeto in listaO:
    for coor in listaO: # for coor in objeto:
        pygame.draw.rect(screen,coor.color,[coor.x,coor.y,30,30])

    for i in range (0,450,30):
        rellenar(screen,(i,0),(i,900))
    for i in range(0,900,30):
        rellenar(screen,(0,i),(450,i))
    #fichaList = posTabl(lista)


    #coll = collis(tablero,fichaList)  # metodo sombra deberia estar detectando por encima y por debajo
    #velocidad = veloc.get(actual.pieza) # ineficiente uso del for
    # al entrar en el for si hay una ficha debajo de un 1 se para de inmediato


    '''
        if bande:
            for elem in lista:
                
                if elem.y >= (ceroY*30)-velocidad: #si hay una ficha debajo de un 1 se para de inmediato porque el valor es mayor que el 1
                    lista = redondear(lista)
                    
                    yMin = minValues(lista,'y')
                    xMin = minValues(lista,'x')
                    xMax = maxValues(lista,'x')
                    lista = posicionar(tablero,lista,xMin,xMax,yMin)
                    lista = cerosTabl(tablero,lista)
                    yMax = maxValues(lista,'y')
                    
                    for objeto in lista:
                        pygame.draw.rect(screen,objeto.color,[objeto.x,objeto.y,30,30])
                        tablero=unos(tablero,int(objeto.y/30),int(objeto.x/30))    
                    row = verificarUnos(tablero)
                    print(row)
                    if len(row) != 0:
                        print(row)
                        listaO = eliminarUnos(listaO,row)
                        tablero = actualizarTablero(tablero,row)
                        listaO = bajarObj(row,listaO)   
                        tablero = bajarUnos(listaO)
                    piece =  gen.randomPieza()
                    color =  gen.colores.get(piece)
                    actual = gen.generaPiece(piece,color)
                    lista = []
                    lista = actual.dibujar(rotacion)
                    for objeto in lista:
                        listaO.append(objeto)
                    m+=1
                    imprimirTablero(tablero)
                    print("________________________________")
                    break
        else:
            
            
            ceroY = verJ(tablero,x,y)
            for elem in lista:
                if elem.y >= (ceroY*30)-velocidad: #si hay una ficha debajo de un 1 se para de inmediato porque el valor es mayor que el 1
                    
                    lista = redondear(lista)
                    lista = cerosTabl(tablero,lista)
                    for objeto in lista:
                        pygame.draw.rect(screen,objeto.color,[objeto.x,objeto.y,30,30])
                        tablero=unos(tablero,int(objeto.y/30),int(objeto.x/30))
                        
                         
                   

                    piece =  gen.randomPieza()
                    color =  gen.colores.get(piece)
                    actual = gen.generaPiece(piece,color)
                    lista = []
                    lista = actual.dibujar(rotacion)
                    for objeto in lista:
                        listaO.append(objeto)
                    m+=1
                    imprimirTablero(tablero)
                    
                     lista = redondear(lista)
                    
                    for objeto in lista:
                        pygame.draw.rect(screen,objeto.color,[objeto.x,objeto.y,30,30])
                        
                        tablero=unos(tablero,int(objeto.y/30),int(objeto.x/30))
                        
                    

                    piece =  gen.randomPieza()
                    color =  gen.colores.get(piece)
                    actual = gen.generaPiece(piece,color)
                    lista = []
                    lista = actual.dibujar()
                    listaO.append(lista)
                    m+=1
                    imprimirTablero(tablero)
                     
                    break
        if m>0:
            break
    '''

    keys = pygame.key.get_pressed()

    if tablero[2][5] == 1:
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