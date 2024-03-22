def number_spiral(fila, columna): 
    matriz = []
    k = 0
    numero = []

    for i in range(fila):
        matriz.append([])

        for j in range(columna):
            numero = matriz[i]
            k = k+1
            # for t in numero :
            matriz[i].append(k)

    
    return matriz



print(number_spiral(2,2))
