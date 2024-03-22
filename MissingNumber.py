def missing_number(n, lista):
    comparar = []#creamos una lista

    #Iteramos la lista "comparar" de i hasta n
    for i in range(n):
        comparar.append(i+1)

    #comparamos listas para encontrar el número faltante
    for i in range(n):
        if comparar[i] != lista[i]:
            return comparar[i]



assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"