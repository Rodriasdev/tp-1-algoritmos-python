def palindrome_reorder(palabra):
    lista_letras = []
    k = 0
    for i in palabra :  
        lista_letras.append(palabra[k])
        k = k + 1
    k=0

    # for i in lista_letras:
        
    #     if lista_letras[k] == lista_letras[k+1]:

    #         print('a')
    #     k=k+1

    pasar_string = ''.join(lista_letras)


    if pasar_string == pasar_string[::-1]:
      return True
    else:
      return False


    return pasar_string


print(palindrome_reorder("soo"))