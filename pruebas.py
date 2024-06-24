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
    anterior = ladosPieza(lista,actual,rotacion,-1)
    siguiente = ladosPieza(lista,actual,rotacion,1)
    """ anterior = True
    siguiente = True """
    """ anterior = True
    siguiente = True """

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                var = lista.copy()
                siguiente = ladosPieza(var,actual,rotacion,1)
                #print(siguiente)
                for elm in lista:
                        print(elm.x)
                        print(elm.y)
                if siguiente == True:
                    print(3)
                    rotacion+=1
                        
                    if rotacion>3:
                        rotacion = 0
                        
                    fichaLi = posTabl(lista)
                    minX = mininX(fichaList) 
                    minY = mininY(fichaList) 
                    lista = actual.rotar(rotacion,lista,minX,minY)
            
            if event.key == pygame.K_z:
                anterior = ladosPieza(lista,actual,rotacion,-1) 
                if anterior== True:
                    rotacion-= 1
                    if rotacion<0:
                        rotacion = 3
                
                    fichaLi = posTabl(lista)
                    minX = mininX(fichaList) 
                    minY = mininY(fichaList) 
                    lista = actual.rotar(rotacion,lista,minX,minY)
            
    # fill the screen with a color to wipe away anything from last frame
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
    fichaList = posTabl(lista)
    #print(fichaList)
    minX = mininX(fichaList) 
    maxX = maxiX(fichaList) 
    un = sombra(tablero,minX,maxX)
    velocidad = veloc.get(actual.pieza)
    # al entrar en el for si hay una ficha debajo de un 1 se para de inmediato
    for i, j in fichaList:
        x = int(i/30)
        y = int(j/30)
        ceroY = un.get(x)
        
        bande = unosJ(tablero,x,y)  # No está revisando si hay fichas encima solo si es mayor que algo, entonces simplementa la corta en el aire cuando detecta el 1
        
        if bande:
            for elem in lista:
                
                if elem.y >= (ceroY*30)-velocidad: #si hay una ficha debajo de un 1 se para de inmediato porque el valor es mayor que el 1
                    lista = redondear(lista)
                    
                    yMin = minYLis(lista)
                    xMin = minXLis(lista)
                    xMax = maxXLis(lista)
                    lista = posicionar(tablero,lista,xMin,xMax,yMin)
                    lista = cerosTabl(tablero,lista)
                    yMax = maxiY(lista)
                    
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
                    
                    """ lista = redondear(lista)
                    
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
                     """
                    break
        if m>0:
            break
    m = 0
    un = {}
    minY = actual.minY(lista)
    minX = actual.minX(lista)
    maxX = actual.maxX(lista)
    keys = pygame.key.get_pressed()

    lista[0].y += 150 * dt    # lista[0].y += 30 * dt 
    lista[1].y += 150 * dt
    lista[2].y += 150 * dt
    lista[3].y += 150 * dt    
    if keys[pygame.K_DOWN]:
        for objeto in lista:
            y = objeto.y
            if y == minY:
                if y >= 850:
                    pass
                else:
                    pass
            if y < 870:
                lista[0].y += 100 * dt    # lista[0].y += 30 * dt 
                lista[1].y += 100 * dt
                lista[2].y += 100 * dt
                lista[3].y += 100 * dt         
    if keys[pygame.K_LEFT]:
        
            for objeto in lista:
                x1 = objeto.x
                if x1 == minX:
                    if x1 <= 2:
                        pass
                    else:
                        lista[0].x -= 300 * dt
                        lista[1].x -= 300 * dt
                        lista[2].x -= 300 * dt
                        lista[3].x -= 300 * dt 
                else:
                    pass  

    if keys[pygame.K_RIGHT]:           
        for objeto in lista:
            x2 = objeto.x
            if x2 == maxX:

                if x2 >=420:
                    pass
                else:

                    lista[0].x += 300 * dt
                    lista[1].x += 300 * dt
                    lista[2].x += 300 * dt
                    lista[3].x += 300 * dt

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