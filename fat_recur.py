def fatorial(a):
    if a == 1:
        return 1
    else:
        print(a)
        return a * fatorial(a-1)

print(fatorial(4))

def busca_bin(lista, item):
    inf = 0 
    sup = len(lista) - 1
    contador = 0
    while inf <= sup:
        contador+=1
        meio = (sup + inf) // 2
        busca = lista[meio]
        print(f"Meio = {meio}, Contador = {contador}")
        if busca == item:
            return f"Item: {meio}"
        if busca > item:
            sup = meio - 1
        else:
            inf = meio + 1
    return None

busca_bin([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 13)

