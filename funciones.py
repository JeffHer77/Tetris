import pygame
import math
listaY = {0:0,1:30,2:60,3:90,4:120,5:150,6:180,7:210,8:240,9:270,10:300,11:330,12:360,13:390,14:420,15:450,16:480,17:510,18:540,19:570,20:600,21:630,
          22:660,23:690,24:720,25:750,26:780,27:810,28:840,29:870,30:900}
listaX = {0:0,1:30,2:60,3:90,4:120,5:150,6:180,7:210,8:240,9:270,10:300,11:330,12:360,13:390,14:420,15:450}
veloc = {'eled':8,'elei':8,'cuadrado':20,'l':20,'t':10,'s':10,'z':10}
def rellenar(screen,x,y):
    pygame.draw.line(screen, (34, 29, 45), [x[0], x[1]], [y[0],y[1]], 1)
    
def tablero():
    matrix = []
    for i in range (0,930,30):
        matr = []
        for j in range (0,450,30):
            matr.append(0)
        matrix.append(matr)
    return matrix

def redondear (lista):
    for elemento in lista:
        x = elemento.x
        y = elemento.y
        if x <0: 
            x =0
        if y <0:
            y=0
        redX = math.floor(x)
        redY = math.floor(y)
        resX = x-redX
        resY = y-redY
        if resX >= 0.5:
            x =math.ceil(x) 
            #print("X redonde " +str(x))
            decimalX = x/30 
            redX = math.floor(decimalX)
            resX = decimalX - redX
            if resX >= 0.5:
                redonX = math.ceil(x/30)
                #print("RedonX es C"+str(redonX)) 
            else:
                redonX = math.floor(x/30)
                #print("RedonX es F "+str(redonX)) 
        else:
            x =math.floor(x) 
            #print("X redonde " +str(x))
            decimalX = x/30 
            redX = math.floor(decimalX)
            resX = decimalX - redX
            if resX >= 0.5:
                redonX = math.ceil(x/30)
                #print("RedonX es C "+str(redonX)) 
            else:
                redonX = math.floor(x/30)
                #print("RedonX es F "+str(redonX)) 
        if resY >= 0.5:
            y =math.ceil(y) 
            #print("Y redonde " +str(y))
            decimalY = y/30 
            redY = math.floor(decimalY)
            resy = decimalY - redY
            if resy >= 0.5:
                redonY = math.ceil(y/30)
                #print("RedonY es C "+str(redonY)) 
            else:
                redonY = math.floor(y/30)
                #print("RedonY es F "+str(redonY)) 
        else:
            y =math.floor(y) 
            #print("Y redonde " +str(y))
            decimalY = y/30 
            redY = math.floor(decimalY)
            resy = decimalY - redY
            if resy >= 0.5:
                redonY = math.ceil(y/30)
                #print("RedonY es C "+str(redonY)) 
            else:
                redonY = math.floor(y/30)
                #print("RedonY es F "+str(redonY)) 
        #print("res X es "+str(resX)+ " res Y es " +str(resY))        
        elemento.x = listaX.get(redonX)
        elemento.y = listaY.get(redonY)
    return lista

def posTabl (lista):
    posList = []
    
    for elemento in lista:
        i = elemento.x
        j = elemento.y
        if i <0: 
            i =0
        if j <0:
            j=0
        redX = math.floor(i)
        redY = math.floor(j)
        resX = i-redX
        resY = j-redY
        if resX >= 0.5:
            i =math.ceil(i) 
            #print("X redonde " +str(i))
            decimalX = i/30 
            redX = math.floor(decimalX)
            resX = decimalX - redX
            if resX >= 0.5:
                redonX = math.ceil(i/30)
                #print("RedonX es C"+str(redonX)) 
            else:
                redonX = math.floor(i/30)
                #print("RedonX es F "+str(redonX)) 
        else:
            i =math.floor(i) 
            #print("X redonde " +str(x))
            decimalX = i/30 
            redX = math.floor(decimalX)
            resX = decimalX - redX
            if resX >= 0.5:
                redonX = math.ceil(i/30)
                #print("RedonX es C "+str(redonX)) 
            else:
                redonX = math.floor(i/30)
                #print("RedonX es F "+str(redonX)) 
        if resY >= 0.5:
            j =math.ceil(j) 
            #print("Y redonde " +str(y))
            decimalY = j/30 
            redY = math.floor(decimalY)
            resy = decimalY - redY
            if resy >= 0.5:
                redonY = math.ceil(j/30)
                #print("RedonY es C "+str(redonY)) 
            else:
                redonY = math.floor(j/30)
                #print("RedonY es F "+str(redonY)) 
        else:
            j =math.floor(j) 
            #print("Y redonde " +str(y))
            decimalY = j/30 
            redY = math.floor(decimalY)
            resy = decimalY - redY
            if resy >= 0.5:
                redonY = math.ceil(j/30)
                #print("RedonY es C "+str(redonY)) 
            else:
                redonY = math.floor(j/30)
                #print("RedonY es F "+str(redonY)) 
        #print("res X es "+str(resX)+ " res Y es " +str(resY)) 
        tup = (listaX.get(redonX),listaY.get(redonY))
        posList.append(tup)
    
    return posList

def unos(tablero,row,col):
    tablero[row][col] = 1
    return tablero
    
def imprimirTablero(tablero):
    for row in tablero:
        for col in row:
            print(col, end=" ")
        print()

    
    

def ordenar(tablero):
    min = {}
    for i in range(0,len(tablero[0]),1):
        for j in range(0,len(tablero),1):
            valor = tablero[j][i]
            if valor == 1:
                min[i] = j
                break
    return min 
            
def sombra(tablero,ini,fin):
    min = {} 
    valor = 0
    for i in range(ini,fin+1,1):
        for j in range(0,len(tablero),1):
            valor = tablero[j][i]
            if valor == 1:
                min[i] = j
                break
        """ if valor == 0:
            min[i]= 30 """
    """ if min == {}:
        for i in range(ini,fin+1,1):
            min[i]= 29 """
    return min 

def maxiX(lista):
        max = 0
        for i in range (0,len(lista),1):
            x = int(lista[i][0]/30)
            if x> max:
                max = x
        return max
def mininX(lista):
        min = 1000
        for i in range (0,len(lista),1):
            x = int(lista[i][0]/30)
            if x< min:
                 min = x
        return min

def minXLis(lista):
    min = 1000
    for objeto in lista:
        x = int(objeto.x/30)
        if x< min:
             min = x
    return min

def maxXLis(lista):
    max = 0
    for objeto in lista:
        x = int(objeto.x/30)
        if x> max:
            max = x
    return max
def maxiY(lista):
    max = 0
    for i in range (0,len(lista),1):
        y = int(lista[i].y/30)
        if y> max:
                max = y
    return max

def maxiYTup(tupla):
    max = 0
    for i in range (0,len(tupla),1):
        y = int(tupla[i][1]/30)
        if y> max:
                max = y
    return max


def mininY(lista):
    min = 1000
    for i in range (0,len(lista),1):
        y = int(lista[i][1]/30)
        if y< min:
            min = y
    return min
def minYLis(lista):
    min = 1000
    for objeto in lista:
        y = int(objeto.y/30)
        if y< min:
            min = y
    return min
""" def mininY(lista):
    min = 1000
    for i in range (0,len(lista),1):
        y = int(lista[i])
        if y< min:
            min = y
    return min """

def unosJ(tablero,pos,posy): # el ciclo se corta cuando j es mayor que cero sin ver si hay fichas encima o no
    valor = 0
    encima = 0
    res = True
    for j in range(0,len(tablero),1):
        valor = tablero[j][pos]
        if valor == 1:
            if j < posy:
                encima = valor
        if 1 == encima:
            res = False
    return res

def verJ(tablero,pos,posy):
    valor = 0
    min = 40
    for j in range(0,len(tablero),1):
        valor = tablero[j][pos]
        if valor == 1: 
            if j < min and j > posy:
                min = j
                
    return min

def cerosTabl(tablero,lista):
    for objeto in lista:
        x = int(objeto.x/30)
        y = int(objeto.y/30)
        valor = tablero[y][x]
        if valor == 1:
            lista[0].y = (lista[0].y-30)
            lista[1].y = (lista[1].y-30)
            lista[2].y = (lista[2].y-30)
            lista[3].y = (lista[3].y-30)
    return lista

def posicionar (tablero,lista,menX,maxX,menY):   # La verificacion de la columna y espacios a deplazar ese puede hacer con el i y j para restarlos
    posi = 0
    for i in range (menX,maxX+1,1):
        for j in range (menY,len(tablero),1):
            valor = tablero[j][i]
            if valor == 1:
                y = j 
                for objeto in lista:
                    valY = objeto.y /30
                    if  y-valY -1 <= 1:
                        posi = y-valY-1
                        break
            if posi != 0:
                break
        if posi != 0:
            break
    for i in range(0,len(lista),1): # posi-1 da la coordenada donde se pone
        y = lista[i].y
        lista[i].y = int(y+(posi*30))
    return lista

def verificarUnos(tablero):
    total = 0
    j = 0
    lista = []
    for i in range(0,30,1):
        total = tablero[i].count(1)
        if total == 15:
            lista.append(i)
            
        j+=1
    return lista

def eliminarUnos(listaObjects,filaList):
    borrar = []
    for i in range (0,len(listaObjects),1):
        y = int(listaObjects[i].y/30)
        for elem in filaList:    
            if y == elem:
                    borrar.append(i)
    borrar.sort(reverse=True)
    for elem in borrar:
        listaObjects.pop(elem)
    return listaObjects

def actualizarTablero(tablero,rows):
    for i in range(0,15,1):
        for j in range (0,len(rows),1):
            tablero[rows[j]][i] = 0
    return tablero

def bajarObj(lineas,listaObj):
    
    for bloques in listaObj:
        lineaY = bloques.y
        for linea in lineas:
            if lineaY < linea*30:
                bloques.y = bloques.y + 30
    return listaObj

def bajarUnos(listaObj):
    table = tablero()
    for i in range (0,15,1):
        table = unos(table,30,i)
    for bloques in listaObj:
        lineaY = int(bloques.y /30)
        colX = int(bloques.x/30)
        table = unos(table,lineaY,colX)
    return table


def posLado(pieza):
    for elemento in pieza:
        x = elemento.x
        if x <0: 
            x =0
        redX = math.floor(x)
        resX = x-redX
        if resX >= 0.5:
            x =math.ceil(x) 
            #print("X redonde " +str(x))
            decimalX = x/30 
            redX = math.floor(decimalX)
            resX = decimalX - redX
            if resX >= 0.5:
                redonX = math.ceil(x/30)
                #print("RedonX es C"+str(redonX)) 
            else:
                redonX = math.floor(x/30)
                #print("RedonX es F "+str(redonX)) 
        else:
            x =math.floor(x) 
            #print("X redonde " +str(x))
            decimalX = x/30 
            redX = math.floor(decimalX)
            resX = decimalX - redX
            if resX >= 0.5:
                redonX = math.ceil(x/30)
                #print("RedonX es C "+str(redonX)) 
            else:
                redonX = math.floor(x/30)
                #print("RedonX es F "+str(redonX)) 
        elemento.x = listaX.get(redonX)
    return pieza

def ladosPieza(lista,pieza,rotacion,move):
    rotacion = rotacion + move
    Band = False
    minI = minXLis(lista)
    minJ = minYLis(lista)
    if rotacion <0:
        rotacion = 3
    elif rotacion > 3:
        rotacion = 0
    cubos = pieza.rotar(rotacion,lista,minI,minJ)
    for bloque in cubos:
        if bloque.x > 0 and bloque.x<420:
            Band = True 
        else:
            Band = False
            break
    print("Bool"+str(cubos == lista))
    return Band

