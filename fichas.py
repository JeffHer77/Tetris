import random
class Bloque:
    ancho = 30
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color

class Pieza:

    listPie = ['eled','elei','cuadrado',
                'l', 't','z','s']
    piezas = { 
        'eled': [ [ [1,0],[1,0],[1,1]],
                 [ [0,0,1],[1,1,1]],
                 [ [1,1],[0,1],[0,1]],
                 [ [1,1,1],[1,0,0]]
                 ],
        'elei': [ [[0,1],[0,1],[1,1]],
                  [ [1,1,1],[0,0,1]],
                  [ [1,1],[1,0],[1,0]],
                  [ [1,0,0],[1,1,1]]
                 ],
        'cuadrado': [[ [1,1], [1,1]]],
        'l': [ [[1,0], [1,0], [1,0], [1,0]],
               [ [1,1,1,1]]
               ],
        't': [[ [1,1,1],[0,1,0]],
              [ [1,0],[1,1],[1,0]],
              [ [0,1,0],[1,1,1]],
              [ [0,1],[1,1],[0,1]]
              ],
        'z': [ [[1,1,0],[0,1,1]],
               [ [0,1],[1,1],[1,0]]
              ],
        's': [[ [0,1,1],[1,1,0]],
              [ [1,0],[1,1],[0,1]]
              ]
        
    }

    colores = { 
        'eled': 'yellow',
        'elei': 'red',
        'cuadrado': 'blue',
        'l': 'cyan',
        't': 'green',
        'z': (218,238,113),
        's': (244,141,73)
        
    }


    def __init__(self,x,y,piece,colour):
        self.x = x
        self.y = y
        self.pieza = piece
        self.color = colour

  



   
    def dibujar(self,rota):
        lista = []
        if self.pieza == 'cuadrado':
            rota = 0
        elif self.pieza == 'l':
           
            if rota%2 == 0:
                rota =1
            else:
                rota = 0
        elif self.pieza == 'z': 

            if rota%2 == 0:
                rota =1
            else:
                rota = 0
        elif self.pieza == 's': 
            if rota%2 == 0:
                rota =1
            else:
                rota = 0
        
        for i in range (0,len(self.piezas.get(self.pieza)[rota]),1):
            for j in range (0,len(self.piezas.get(self.pieza)[rota][0]),1):
                valor = 30*self.piezas.get(self.pieza)[rota][i][j]*(j+1)
                if valor != 0:
                    m = len(self.piezas.get(self.pieza)[rota][0])
                    n = len(self.piezas.get(self.pieza))
                    #print("i va hasta "+str(n) +" j va hasta "+str(m))
                    cuadro = Bloque(30*self.piezas.get(self.pieza)[rota][i][j]*(j+1)+self.x,30*self.piezas.get(self.pieza)[rota][i][j]*(i+1)+self.y,self.color)
                    lista.append(cuadro)
                else:
                    pass
        #print("Lar lista "+str(len(lista)))
        return lista
    
    def rotar(self,rota,lista,x,y):
        if self.pieza == 'cuadrado':
            rota = 0
        elif self.pieza == 'l':
            
            if rota%2 == 0:
                rota =1
            else:
                rota = 0
        elif self.pieza == 'z': 
            if rota%2 == 0:
                rota =1
            else:
                rota = 0
        elif self.pieza == 's': 
            if rota%2 == 0:
                rota =1
            else:
                rota = 0
        increm = 0
        forma = self.piezas.get(self.pieza)[rota]
        for i in range(0,len(forma),1):
            for j in range(0,(len(forma[0])),1):
                # [[1,1,0],[0,1,1]]
                # [ [0,1],[1,1],[1,0]]
                value = forma[i][j]
                if value == 1:
                    lista[increm].x = forma[i][j]*(j+x)*30
                    lista[increm].y = forma[i][j]*(i+y)*30
                    increm+=1
        return lista

    def maxX(self,lista):
        max = 0
        for objeto in lista:
            x = objeto.x
            if x> max:
                max = x
        return max
    def minX(self,lista):
        min = 1000
        for objeto in lista:
            x = objeto.x
            if x< min:
                min = x
        return min
    
    def minY(self,lista):
        min = 0
        for objeto in lista:
            x = objeto.y
            if x> min:
                min = x
        return min
    

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

    listPie = ['eled','elei','cuadrado',
                    'l', 't','z','s']

    def randomPieza(self):
            pieza = random.choice(self.listPie)
            return pieza    

    def generaPiece(self,pieza,color):
        return Pieza(self.x,self.y,pieza,color)
    
        
    

def nueva (x1,x2,x3,x4,y1,y2,y3,y4):
    pieza = Pieza(x1,x2,x3,x4+30,y1,y2,y3,y4)
    return pieza

