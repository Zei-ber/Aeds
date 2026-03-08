import random
import time
import matplotlib.pyplot as plt


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Heap Sort
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
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Teste com n=10000
n = 10000
dados = [random.randint(0, 100000) for _ in range(n)]

# Bubble
arr1 = dados.copy()
inicio = time.time()
bubble_sort(arr1)
tempo_bubble = time.time() - inicio

# Heap
arr2 = dados.copy()
inicio = time.time()
heap_sort(arr2)
tempo_heap = time.time() - inicio

# Gráfico
plt.bar(["Bubble Sort", "Heap Sort"], [tempo_bubble, tempo_heap], color=["red", "blue"])
plt.title("Comparação - Grandes Dados (n=10.000)")
plt.ylabel("Tempo (segundos)")
plt.show()