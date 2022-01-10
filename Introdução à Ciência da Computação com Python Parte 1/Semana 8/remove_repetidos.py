def remove_repetidos(lista):
    lista.sort()
    print(lista)
    for i in range(len(lista)-1,0,-1):
        print(i)
        if lista[i] == lista[i-1]:
            del lista[i]
    
    return lista