import os
def camino(grafo, inicio, final):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    camino_mas_corto = {}
    visitados = set()

    while visitados != set(grafo):
        actual = None
        min_distancia = float('inf')
        for nodo in grafo:
            if nodo not in visitados and distancias[nodo] < min_distancia:
                actual = nodo
                min_distancia = distancias[nodo]
        visitados.add(actual)
        for nodo_adyacente, (distancia, calle) in grafo[actual].items():
            distancia_total = distancias[actual] + distancia
            if distancia_total < distancias[nodo_adyacente]:
                distancias[nodo_adyacente] = distancia_total
                camino_mas_corto[nodo_adyacente] = (actual, calle)

    camino = [final]
    nodo = final
    while nodo != inicio:
        nodo_previo, calle = camino_mas_corto[nodo]
        camino.append(nodo_previo)
        nodo = nodo_previo
    camino.reverse()
    distancia = distancias[final]

    print("Camino más corto:")
    for i in range(len(camino)-1):
        nodo_actual = camino[i]
        nodo_siguiente = camino[i+1]
        calle = grafo[nodo_actual][nodo_siguiente][1]
        print(nodo_actual, " -> ", nodo_siguiente, " (por", calle, ")")

    print("Distancia:", distancia,"m")

grafo = {
    'A': {'B': (82, 'Prol. Ferrocarril'), 'E': (70, 'Calle Junin')},
    'B': {'A': (82, 'Prol. Ferrocarril'), 'C': (76, 'Prol. Ferrocarril'), 'G': (65, 'Calle Callao')},
    'C': {'B': (76, 'Prol. Ferrocarril'), 'F': (58, 'Jirón Moquegua')},
    'D': {'V': (32, 'Calle Matará')},
    'E': {'H': (70, 'Calle Junin'), 'A': (70, 'Calle Junin')},
    'F': {'C': (58, 'Jirón Moquegua'),'G': (77, 'Calle Matará'), 'J': (78, 'Jirón Moquegua')},
    'G': {'E': (79, 'Calle Matará'), 'I': (75, 'Calle Callao')},
    'H': {'E': (70, 'Calle Junin'), 'U': (33, 'Calle Junin')},
    'I': {'H': (80, 'Calle Mirave'), 'N': (38, 'Calle Callao')},
    'J': {'O': (43, 'Jirón Moquegua'), 'I': (77, 'Calle Mirave')},
    'K': {'J': (52, 'Calle Mirave'), 'V': (76, 'C. Zepita')},
    'L': {'D': (77, 'Jr. Abtao'), 'K': (38, 'Calle Mirave')},
    'M': {'K': (38, 'C. Zepita')},
    'N': {'O': (77, '2 de mayo'), 'R': (75, 'Calle Callao'), 'U': (82, '2 de mayo')},
    'O': {'M': (76, '2 de mayo'),'N': (77, '2 de mayo'), 'S': (76, 'Jirón Moquegua')},
    'P': {'R': (82, 'Av. 28 de Julio'), 'U': (77, 'Calle Junin')},
    'Q': {'L': (113, 'Jr. Abtao'), 'T': (52, 'Av. 28 de Julio')},
    'R': {'N': (75, 'Calle Callao'), 'P': (82, 'Av. 28 de Julio'), 'S': (80, 'Av. 28 de Julio')},
    'S': {'T': (54, 'Av. 28 de Julio'), 'R': (80, 'Av. 28 de Julio')},
    'T': {'M': (113, 'C. Zepita'), 'S': (54, 'Av. 28 de Julio'), 'Q': (52, 'Av. 28 de Julio')},
    'U': {'P': (77, 'Calle Junin'), 'H': (33, 'Calle Junin'), 'N': (82, '2 de mayo')},
    'V': {'F': (51, 'Calle Matará')}
}
while True:
    try:
        inicio = str(input("ingrese en que punto de encuentra: "))
        final = str(input("ingrese a que punto quiere llegar: "))
        camino(grafo, inicio.upper(), final.upper())
        break
    except:
        os.system("cls")
        print("ingrese datos validos, (A-V)")
