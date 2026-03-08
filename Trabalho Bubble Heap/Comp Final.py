import time
import random
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr

# Heap Sort
def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Testes de tempo
def testar(n):
    arr = [random.randint(0, 10000) for _ in range(n)]
    # Bubble
    copia = arr[:]
    inicio = time.time()
    bubble_sort(copia)
    tempo_bubble = time.time() - inicio
    # Heap
    copia = arr[:]
    inicio = time.time()
    heap_sort(copia)
    tempo_heap = time.time() - inicio
    return tempo_bubble, tempo_heap

# Rodando os testes
tamanhos = [100, 1000, 10000]
resultados_bubble = []
resultados_heap = []

for n in tamanhos:
    tb, th = testar(n)
    resultados_bubble.append(tb)
    resultados_heap.append(th)

# Plot
plt.plot(tamanhos, resultados_bubble, label="Bubble Sort")
plt.plot(tamanhos, resultados_heap, label="Heap Sort")
plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo (s)")
plt.legend()
plt.show()