import random
import pygame
import math

class Bloque:
    ancho = 30
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color

    def __getitem__(self, item):
        if item == "x":
            return self.x
        elif item == "y":
            return self.y
        else:
            return None

class Pieza:




    def __init__(self,x,y,piece,bloques):
        self.bloques = bloques
        self.pieza = piece
        self.color = colores[piece]
        self.forma = matrices[piece]



    def rotar(self, width):

        minX = 1000
        minY = 1000
        maxX = 0
        for bloque in self.bloques:
            x = bloque.x
            y = bloque.y
            if x <= minX:
                minX = x
            if y <= minY:
                minY = y
            if x >= maxX:
                maxX = x

        forma =  [list(row) for row in zip(*self.forma[::-1])]
        nums = []
        i = 0
        for lista in forma:
            for elemento in lista:
                if elemento == 1:
                    nums.append(int(minX+ i*30))
                i +=1
        maximo = max(nums)
        if  maximo >= width - 180:
            self.forma = [list(row) for row in zip(*self.forma[::-1])]

            k = 0
            j = 0
            i = 0


            for lista in self.forma:

                for elemento in reversed(lista):

                    if elemento == 1:
                        self.bloques[k].x =  maxX - i*30
                        self.bloques[k].y =  minY + j*30
                        k+=1
                    i+=1
                j+=1
                i = 0
        else:
            self.forma = [list(row) for row in zip(*self.forma[::-1])]

            k = 0
            j = 0
            i = 0

            for lista in self.forma:

                for elemento in lista:

                    if elemento == 1:

                        self.bloques[k].x = minX + i * 30
                        self.bloques[k].y = minY + j * 30

                        k += 1
                    i += 1
                i = 0
                j += 1

class generar:
    flag = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y =y

    piezas = { 
        'eled': [ [1,0],[1,0],[1,1]],
        'elei': [ [0,1],[0,1],[1,1]],
        'cuadrado': [ [1,1], [1,1]],
        'l': [ [1,0], [1,0], [1,0], [1,0]],
        't': [ [1,1,1],[0,1,0]],
        'z': [ [1,1,0],[0,1,1]],
        's': [ [0,1,1],[1,1,0]]
        
    }

    colores = { 
            'eled': (119,116,6),
            'elei': (120,5,14),
            'cuadrado': (11,109,138),
            'l': (19,130,55),
            't': (123,148,27),
            'z': (105,22,29),
            's': (41,73,39)
            
        }

    def randomPieza(self):
            pieza = random.choice(self.listPie)
            return pieza    

    def generaPiece(self,pieza,color):
        return Pieza(self.x,self.y,pieza,color)
    
        
    
formas = ['eled','elei','cuadrado',
                    'l', 't','z','s']

colores = {
    'eled': (119, 116, 6),
    'elei': (120, 5, 14),
    'cuadrado': (11, 109, 138),
    'l': (19, 130, 55),
    't': (123, 148, 27),
    'z': (105, 22, 29),
    's': (41, 73, 39)

}
matrices = {
    'eled': [[1, 0], [1, 0], [1, 1]],
    'elei': [[0, 1], [0, 1], [1, 1]],
    'cuadrado': [[1, 1], [1, 1]],
    'l': [[1, 0], [1, 0], [1, 0], [1, 0]],
    't': [[1, 1, 1], [0, 1, 0]],
    'z': [[1, 1, 0], [0, 1, 1]],
    's': [[0, 1, 1], [1, 1, 0]]

}


def bloques(forma,color,x,y):
    lista = []

    for i in range(len(forma)):
        for j in range(len(forma[0])):
            valor = 30 * forma[i][j] * (j + 1)
            if valor != 0:

                cuadro = Bloque(30 * forma[i][j] * (j + 1) + x, 30 * forma[i][j] * (i + 1) + y,
                                color)
                lista.append(cuadro)
            else:
                pass
    return lista

def rellenar(screen,x,y):
    pygame.draw.line(screen, (34, 29, 45), [x[0], x[1]], [y[0],y[1]], 1)

def tablero(width, height):   # table = tablero(int(width//30),(int(height+60)//30))

    matrix = []
    for i in range (0,int(height),1):
        matr = []
        for j in range (0,int(width),1):
            matr.append(0)
        matrix.append(matr)
    return matrix

def unos(tablero,row,col):

    tablero[row][col] = 1
    return tablero

def imprimirTablero(tablero):
    for row in tablero:
        for col in row:
            print(col, end=" ")
        print()

# collis necesita objetos pieza
def collis(piece, desfase, width, height,tablero):

    if isinstance(piece, Pieza):
        for bloque in piece.bloques:
            #i=1
            x = int(bloque.x + desfase[0]*30)
            y = int(bloque.y + desfase[1]*30)
            #print('x ' + str(x//30) + ' y ' + str(y//30))
            #print('x ' + str(x//30) + ' y ' + str(y//30))
            #print(tablero[int(y//30)][int(x//30)])
            #print('bloque num '+str(i))
            #i+=1
            # y < 0 or y >= height-35
            if x < 0 or x >= width-30 or y < 0 or y >= height-30:
                return False
    else:
        x = int(piece.x + desfase[0] * 30)
        y = int(piece.y + desfase[1] * 30)
        if x < 0 or x >= width - 30 or y < 0 or y >= height - 30:
            return False

    return True

def collisUnos (objeto, desfase,tablero):
    if isinstance(objeto, Pieza):

        for bloque in objeto.bloques:
            x = int(bloque.x // 30) + desfase[0]
            y = int(bloque.y // 30) + desfase[1]
            if desfase[0] !=0 and tablero[y][x] == 1:
                return False
            elif desfase[1] !=0 and tablero[y][x] == 1:
                return False
    else:

        x = int(objeto.x // 30) + desfase[0]
        y = int(objeto.y // 30) + desfase[1]
        if desfase[0] !=0 and tablero[y][x] == 1:
            return False
        elif desfase[1] !=0 and tablero[y][x] == 1:
            return False

    return True





def verificarUnos(tablero,width,fila):        # lista de las filas llenas

    total = tablero[fila].count(1)
    if total == width//30:

        return True

    return False

def eliminarUnos(listaObjects,fila):
    borrar = []
    for i in range (0,len(listaObjects),1):
        y = int(listaObjects[i].y/30)
        if y in fila:
            borrar.append(i)
    borrar.sort(reverse=True)
    for elem in borrar:
        listaObjects.pop(elem)
    return listaObjects

def actualizarTablero(tablero,fila,width):  # cambiar a ceros los valores de las filas llenas

    for i in range(0,width//30,1):
        tablero[fila][i] = 0
    return tablero

def bajarObj(lineas,listaObj):

    for bloques in listaObj:
        lineaY = bloques.y
        for linea in lineas:
            if lineaY < linea*30:
                bloques.y = bloques.y + 30
    return listaObj

def bajarUnos(listaObj, actual,width, height,table):
    tama = int(len(table))
    table = tablero(int(width//30),int((height+30)//30))
    for i in range(0, width // 30, 1):  # cambiado
        table = unos(table, tama - 1, i)
    for bloque in listaObj:
        x = int(bloque.x//30)
        y = int(bloque.y//30)
        table = unos(table,y,x)
    for bloque in actual:
        x = int(bloque.x//30)
        y = int(bloque.y//30)
        table = unos(table,y,x)
    return table
