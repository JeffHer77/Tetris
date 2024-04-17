import pygame
from fichas import *
from funciones import *
import time
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((450, 900))  #pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
tablero = tablero()
for i in range(0,15,1):
    tablero = unos(tablero,30,i)
imprimirTablero(tablero)
gen = generar(120,-30)
piece =  gen.randomPieza()
color = gen.colores.get('s')
ele = gen.generaPiece('s',color)
lista = ele.dibujar()
actual = ele
listaO =[]
listaO.append(lista)
m =0

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((49,38,75))
    
    #for coor in lista:
        #pygame.draw.rect(screen,color,[coor.x,coor.y,30,30])

    for objeto in listaO:
        for coor in objeto:
            pygame.draw.rect(screen,coor.color,[coor.x,coor.y,30,30])


    for i in range (0,450,30):
        rellenar(screen,(i,0),(i,900))
    for i in range(0,900,30):
        rellenar(screen,(0,i),(450,i))
    fichaList = posTabl(lista)
    minX = mininX(fichaList) 
    maxX = maxiX(fichaList) 
    un = sombra(tablero,minX,maxX)
    # al entrar en el for si hay una ficha debajo de un 1 se para de inmediato
    for i, j in fichaList:
        x = int(i/30)
        y = int(j/30)
        ceroY = un.get(x)
        bande = unosJ(tablero,x,y)  # No está revisando si hay fichas encima solo si es mayor que algo, entonces simplementa la corta en el aire cuando detecta el 1
        
        
        if bande:
            for elem in lista:
                if elem.y >= (ceroY*30)-5: #si hay una ficha debajo de un 1 se para de inmediato porque el valor es mayor que el 1
                    lista = redondear(lista)
                    fichaList = posTabl(lista)
                    minX = mininX(fichaList) 
                    maxX = maxiX(fichaList) 
                    conta = 0
                    ceros = {}
                    print("Antes")
                    for objeto in lista:
                        print("x__: " +str(int(objeto.x/30))+" y___: "+str(int(objeto.y/30)))
                    for k in range(minX,maxX+1,1):
                        ceroY = UnosJDeb(tablero,k,lista[conta].y)
                        ceros[k]= ceroY
                        conta+=1
                    lista = redondUnos(lista,ceros)
                    print("Despues")
                    for objeto in lista:
                        pygame.draw.rect(screen,objeto.color,[objeto.x,objeto.y,30,30])
                        tablero=unos(tablero,int(objeto.y/30),int(objeto.x/30))
                        print("x__: " +str(int(objeto.x/30))+" y___: "+str(int(objeto.y/30)))
                         
                    print(ceros)

                    piece =  gen.randomPieza()
                    color =  gen.colores.get(piece)
                    actual = gen.generaPiece(piece,color)
                    lista = []
                    lista = actual.dibujar()
                    listaO.append(lista)
                    m+=1
                    imprimirTablero(tablero)
                    
                    break
        else:
            
            
            ceroY = verJ(tablero,x,y)
            for elem in lista:
                if elem.y >= (ceroY*30)-17: #si hay una ficha debajo de un 1 se para de inmediato porque el valor es mayor que el 1
                    
                    lista = redondear(lista)
                    fichaList = posTabl(lista)
                    minX = mininX(fichaList) 
                    maxX = maxiX(fichaList) 
                    conta = 0
                    ceros = {}
                    for k in range(minX,maxX+1,1):
                        #tupl = ()
                        ceroY = UnosJDeb(tablero,k,lista[conta].y)
                        #tupl = (k,ceroY)
                        ceros[k]= ceroY
                        conta+=1
                    lista = redondUnos(lista,ceros)
                    for objeto in lista:
                        pygame.draw.rect(screen,objeto.color,[objeto.x,objeto.y,30,30])
                        tablero=unos(tablero,int(objeto.y/30),int(objeto.x/30))
                        print("x__: " +str(int(objeto.x/30))+" y___: "+str(int(objeto.y/30)))
                         
                    print(ceros)

                    piece =  gen.randomPieza()
                    color =  gen.colores.get(piece)
                    actual = gen.generaPiece(piece,color)
                    lista = []
                    lista = actual.dibujar()
                    listaO.append(lista)
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

    




    """ lista[0].y += 150 * dt
    lista[1].y += 150 * dt
    lista[2].y += 150 * dt
    lista[3].y += 150 * dt """
    if keys[pygame.K_DOWN]:
        for objeto in lista:
            y = objeto.y
            if y == minY:
                if y >= 850:
                    pass
                else:
                    pass
            if y < 870:
                lista[0].y += 30 * dt
                lista[1].y += 30 * dt
                lista[2].y += 30 * dt
                lista[3].y += 30 * dt         


    if keys[pygame.K_RIGHT]:
        for objeto in lista:
            x = objeto.x
            if x == maxX:
                if x >=420:
                    pass
                else:
                    lista[0].x += 300 * dt
                    lista[1].x += 300 * dt
                    lista[2].x += 300 * dt
                    lista[3].x += 300 * dt

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
                    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)/1000
    

pygame.quit()





"""     if keys[pygame.K_RIGHT]:
        Boo = restrinLado(tablero,lista)
        if Boo == False:
        lista = restrinLado(tablero, lista)
        for objeto in lista:
            x = objeto.x
            if x == maxX:
                if x >=420:
                    pass
                else:
                    lista[0].x += 300 * dt
                    lista[1].x += 300 * dt
                    lista[2].x += 300 * dt
                    lista[3].x += 300 * dt
"""
""" if keys[pygame.K_LEFT]:
        Boo = restrinLado(tablero,lista)
        if Boo == False:
        lista = restrinLado(tablero, lista)
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
        """