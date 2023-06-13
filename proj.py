import time

#selection sort
def selection_sort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

#bubble sort
def bubble_sort(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#insertion sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    return lista

#merge sort
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

#quick sort
def quick_sort(lista):
    stack = [(0, len(lista) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = lista[high]
            i = low - 1

            for j in range(low, high):
                if lista[j] < pivot:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]

            lista[i + 1], lista[high] = lista[high], lista[i + 1]
            p = i + 1

            stack.append((low, p - 1))
            stack.append((p + 1, high))
    return lista

#ler arquivo e salvar em lista
def lista(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    lista = []
    for linha in arquivo:
        lista.append(int(linha))
    arquivo.close()
    return lista

ar=lista('num.100000.4.in')

#teste de algoritmos
def teste_algoritmos(algoritmo):
    print('teste: ', algoritmo)
    lista = ar
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    print('tempo: ', fim - inicio)



teste_algoritmos(merge_sort)
teste_algoritmos(selection_sort)
teste_algoritmos(quick_sort)
teste_algoritmos(bubble_sort)
teste_algoritmos(insertion_sort)