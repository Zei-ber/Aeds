def bubble_sort_melhorado(arr):
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True
        if not trocou:  # Se não houve troca, já está ordenado
            break

# Exemplo de uso
dados = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_melhorado(dados)
print("Bubble Sort melhorado:", dados)