def heapify(arr, n, i):
    maior = i
    esq = 2*i + 1
    dir = 2*i + 2

    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    # Construir heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extrair elementos do heap
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Exemplo de uso
dados = [64, 34, 25, 12, 22, 11, 90]
heap_sort(dados)
print("Heap Sort:", dados)