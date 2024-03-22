def weird_algorithm(n):
    
    lista = [n] #Se crea una lista en donde se guardaran los números

    #Verifica si el número es mayor a uno
    if n > 1 :

        #Verifica si el número es muy grande
        if n < 10**6:

            #Utilizamos un bucle para realizaz las operaciones hasta que "n" sea igual a uno
            while n != 1:
                #Verifica si el número es par, sino  ejecuta el else.
                if n % 2 == 0:
                    n = n / 2
                    lista.append(n)#Guardamos el valor al final de la lista
                else : 
                    n = (n*3) + 1
                    lista.append(n)#Guardamos el valor al final de la lista

            return lista #
        else:
            print('El número es muy grande.')
    else: 
       print('El número debe ser mayor a uno.')

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1] , "Error en el caso de prueba"