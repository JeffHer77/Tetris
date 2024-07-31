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

def posTabl (listac):
    posList = []
    lista = listac[:]
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

    
    

def collis(tablero,bloques):
    
    parejas = []
    xBf = -1
    xAft = -1
    yBf = -1
    yAft = -1

    for i, j in bloques:

        #print("i " + str(i) + " j " + str(j) )

        if (i > 0  and i <= 390):  # verificar caso donde i es cero


            xBf = tablero[int(j/30)][int((i/30)-1)]
            xAft = tablero[int(j/30)][int((i/30)+1)]

            if (j > 0):
                yBf = tablero[int((j/30)-1)][int(i/30)]
                yAft = tablero[int((j/30)+1)][int(i/30)]
        else: # caso donde i es cero menor que o mayor a 390

            if (i > 390):
                xBf = tablero[int(j / 30)][int((i / 30) - 1)]

            if (i == 0):
                xAft = tablero[int(j / 30)][int((i / 30) + 1)]
            if j > 0:
                yBf = tablero[int((j/30) - 1)][int(i/30)]
                yAft = tablero[int((j/30) + 1)][int(i/30)]

        if xBf == 1:

            par = (int((i/30)-1), int(j/30))
            parejas.append(par)

        elif xAft == 1:
            par = (int((i / 30) + 1) , int(j / 30))
            parejas.append(par)

        elif yBf == 1:
            par = (int(i / 30), (int(j/30) - 1))
            parejas.append(par)

        elif yAft == 1:
            par = (int(i / 30), (int(j / 30) + 1))
            parejas.append(par)

        elif xBf == -1 or xBf == 0:
            par = (-1,-1)
            parejas.append(par)

        elif xAft == -1 or xAft == 0:
            par = (-1,-1)
            parejas.append(par)

        elif yBf == -1 or yBf == 0:
            par = (-1, -1)
            parejas.append(par)

        elif yAft == -1 or yAft == 0:
            par = (-1,-1)
            parejas.append(par)

    return parejas
def minValues(paquete, valor,indice=0):
    min = 1000
    if valor == 'x' or  valor == 'y':
        for objeto in paquete:
            aux = int(objeto[valor] / 30)
            if aux < min:
                min = aux
    elif valor == 'tup':
        for i in range(0, len(paquete), 1):
            aux = int(paquete[i][indice] / 30)
            if aux < min:
                min = aux
    return min

def maxValues(paquete, valor, indice=0):
    max = 0
    if valor == 'x' or valor == 'y':
        for objeto in paquete:
            aux = int(objeto[valor]/30)
            if aux> max:
                    max = aux
    elif valor == 'tup':
        for i in range(0, len(paquete), 1):
            aux = int(paquete[i][indice] / 30)
            if aux > max:
                max = aux
    return max
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
    lista = []

    for i in range(0,30,1):
        total = tablero[i].count(1)
        if total == 15:
            lista.append(i)


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
    rotacionX = rotacion + move
    Band = False
    minI = minValues(lista, 'x')
    minJ = minValues(lista, 'y')
    if rotacionX <0:
        rotacionX = 3
    elif rotacionX > 3:
        rotacionX = 0
    valX = []
    valY = []
    for bloques in lista:
        valX.append(bloques.x)
        valY.append(bloques.y)
    if pieza.pieza == 'cuadrado':
        rotacionX = 0
    elif pieza.pieza == 'l':

        if rotacionX%2 == 0:
            rotacionX =1
        else:
            rotacionX = 0
    elif pieza.pieza == 'z':
        if rotacionX%2 == 0:
            rotacionX =1
        else:
            rotacionX = 0
    elif pieza.pieza == 's':
        if rotacionX%2 == 0:
            rotacionX = 1
        else:
            rotacionX = 0
            #increm = 0
    forma = pieza.piezas.get(pieza.pieza)[rotacionX]
    for i in range(0,len(forma),1):
        y = 0
        for j in range(0,(len(forma[0])),1):
                    # [[1,1,0],[0,1,1]]
                    # [ [0,1],[1,1],[1,0]]
            value = forma[i][j]
            if value == 1:
                valX[y] = value*(j+minI)*30
                valY[y] = value*(i+minJ)*30

                y += 1

    for coor in valX:
        if coor > 0 and coor < 450:
            Band = True
        else:
            Band = False
            break
    return Band




'''
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 
0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 
0 0 0 0 0 0 0 0 1 1 1 1 0 1 1 
1 0 0 0 0 0 0 0 1 1 1 1 0 0 1 
1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 
1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 
1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 


'''