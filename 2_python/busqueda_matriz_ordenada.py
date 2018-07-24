def show(matrix):
    for row in matrix:
        print row

def promedio(inicio, fin):
    return (inicio+fin)//2

def get(matriz, coordenada):
    ancho = len(matriz[0])
    return matriz[ coordenada//ancho ][coordenada % ancho]

def busqueda_matriz_ordenada(matriz, elemento):
    print("buscando {}...".format(elemento))
    inicio = 0
    fin = len(matriz)*len(matriz[0]) - 1
    medio = promedio(inicio, fin)
    while inicio <= fin:
        if get(matriz, medio) > elemento:
            fin = medio - 1
        elif get(matriz, medio) < elemento:
            inicio = medio + 1 
        else:
            return True
        medio = promedio(inicio, fin)
    return False

m = [ [1, 2 , 4],
      [8, 16, 32],
      [64, 128, 256] ]

show(m)
print(busqueda_matriz_ordenada(m, 1))
print(busqueda_matriz_ordenada(m, 5))

