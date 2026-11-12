import random

def ha_comido_serpiente(serpiente: list[tuple[int, int]], posicion_comida: tuple[int, int]) -> bool:
    '''
    Comprueba si la cabeza de la serpiente está en la misma posición que la comida.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    posicion_comida: Tupla representando la posición de la comida (columna, fila).

    Devuelve:
    True si la cabeza de la serpiente está en la misma posición que la comida, False en caso contrario.
    '''
    if serpiente[0] == posicion_comida:
        return True
    else:
        return False

def comprueba_choque(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]]) -> bool:
    '''
    Comprueba si la serpiente se ha chocado consigo misma o con las paredes. Tenga en cuenta
    que la serpiente avanza siempre por su cabeza, que está situada en la 
    primera posición de la lista.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de cada segmento de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.

    Devuelve:
    True si la serpiente se ha chocado consigo misma o con las paredes, False en caso contrario.
    '''
    for i in serpiente[1:]: #i son los elemntos dentro de serpiente
        if i == serpiente[0]:
            return True
    for j in paredes:
        for x in j: #j ya es una lista
            if x == serpiente[0]:
                return True
    return False

def crece_serpiente(serpiente: list[tuple[int, int]]) -> None:
    '''
    Hace crecer la serpiente añadiendo duplicando la posición de la cola

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    '''
    serpiente.append(serpiente[-1]) #cuidado no poner los dos puntos aquí, porque estas llendo a una posición, no a recorrer a partir de ahí la lista

def genera_comida_aleatoria(serpiente: list[tuple[int, int]], paredes: list[list[tuple[int, int]]], filas: int, columnas: int) -> tuple[int, int]:
    '''
    Genera una posición aleatoria para la comida que no esté en la misma posición que la serpiente o las paredes.

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    paredes: Lista de listas de tuplas representando las posiciones (columna, fila) de los segmentos de las paredes.
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.

    Devuelve:
    Posición aleatoria para la comida (columna, fila).
    '''
    n1 = 0
    n2 = 0
    verdad = False
    while verdad == False:
        n1 = random.randint(0,filas - 1) #filas
        n2 = random.randint(0, columnas -1) #columnas
        verdad = True
        for i in serpiente:
            if i == (n2,n1):
                verdad = False
        for j in paredes:
            for x in j:
                if x ==(n2,n1):
                    verdad = False
    return (n2,n1)

def mueve_serpiente(serpiente: list[tuple[int, int]], direccion: str, filas: int, columnas: int) -> None:
    '''
    Mueve la serpiente en el tablero según la dirección dada. El tablero es circular, lo que significa
    que si la serpiente se sale por la derecha, debe aparecer por la izquierda, y viceversa (y lo 
    mismo si se sale por arriba o por abajo).

    Parámetros:
    serpiente: Lista de tuplas representando las posiciones (columna, fila) de la serpiente.
    direccion: Dirección en la que se debe mover la serpiente ('Left', 'Right', 'Down', 'Up').
    filas: Número de filas en el tablero de juego.
    columnas: Número de columnas en el tablero de juego.
    '''
    if direccion == 'Right':
        serpiente.insert(0,((serpiente[0][0]+1)% columnas, serpiente[0][1]))
    if direccion == 'Left':
            serpiente.insert(0,((serpiente[0][0]-1)% columnas, serpiente[0][1]))
    if direccion == 'Up':
            serpiente.insert(0,(serpiente[0][0], (serpiente[0][1] -1 )% filas))
    if direccion == 'Down':
            serpiente.insert(0,(serpiente[0][0], (serpiente[0][1] + 1) % filas))
    del serpiente[-1] #eliminas la posición dentro de la lista de la memoria


