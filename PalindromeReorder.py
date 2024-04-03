def palindrome_reorder(palabra):
    frecuencia_letra = {}
    impares = []
    mitad_izquierda = ''
    mitad_derecha = ''

    # Contamos con qué frecuencia se repite cada letra
    for i in palabra:
        if i in frecuencia_letra:
            frecuencia_letra[i] += 1
        else:
            frecuencia_letra[i] = 1

    # Guardamos en una lista las letras que se repiten con frecuencia impar
    for clave, valor in frecuencia_letra.items():
        if valor % 2 != 0:
            impares.append(clave)

    # Terminamos la ejecución si hay más de 1 letra con frecuencia impar 
    if len(impares) > 1:
        return "NOT SOLUTION"

    # Construimos la mitad izquierda concatenando las letras repetidas a la mitad de su frecuencia.
    for clave, valor in frecuencia_letra.items():
        mitad_izquierda += clave * (valor // 2)

    # Construimos la mitad derecha invirtiendo la mitad izquierda
    mitad_derecha = mitad_izquierda[::-1]

    # Concatenamos la mitad izquierda con la letra impar (si existe), y la mitad derecha.
    palindromo = mitad_izquierda + (impares[0] if impares else '') + mitad_derecha

    return palindromo


assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"