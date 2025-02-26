import time
import math

def insertion_sort(arr, esquerda, direita, etapas):
    """ordena o array usando insertion sort."""
    for i in range(esquerda + 1, direita + 1):
        chave = arr[i]
        j = i - 1
        while j >= esquerda and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
            etapas[0] += 1  # conta cada troca
        etapas[0] += 1  # conta cada comparação
        arr[j + 1] = chave

def heapify(arr, n, i, etapas):
    """transforma um subárvore enraizada no índice 'i' em um heap máximo."""
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda
    etapas[0] += 1  # conta cada comparação

    if direita < n and arr[direita] > arr[maior]:
        maior = direita
    etapas[0] += 1  # conta cada comparação

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        etapas[0] += 1  # conta cada troca
        heapify(arr, n, maior, etapas)

def heap_sort(arr, esquerda, direita, etapas):
    """ordena o array usando heap sort."""
    n = direita - esquerda + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, etapas)
    for i in range(n - 1, 0, -1):
        arr[esquerda + i], arr[esquerda] = arr[esquerda], arr[esquerda + i]
        etapas[0] += 1  # conta cada troca
        heapify(arr, i, 0, etapas)

def particionar(arr, esquerda, direita, etapas):
    """particiona o array usando o último elemento como pivô."""
    pivo = arr[direita]
    i = esquerda - 1
    for j in range(esquerda, direita):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            etapas[0] += 1  # conta cada troca
        etapas[0] += 1  # conta cada comparação
    arr[i + 1], arr[direita] = arr[direita], arr[i + 1]
    etapas[0] += 1  # conta cada troca
    return i + 1

def introsort(arr, esquerda, direita, profundidade_max, etapas):
    """implementação do introsort."""
    tamanho = direita - esquerda + 1
    if tamanho < 16:  # usa insertion sort para pequenos subarrays
        insertion_sort(arr, esquerda, direita, etapas)
    elif profundidade_max == 0:  # alterna para heap sort se a profundidade máxima for atingida
        heap_sort(arr, esquerda, direita, etapas)
    else:
        pivo_idx = particionar(arr, esquerda, direita, etapas)
        introsort(arr, esquerda, pivo_idx - 1, profundidade_max - 1, etapas)
        introsort(arr, pivo_idx + 1, direita, profundidade_max - 1, etapas)

def ler_valores():
    """lê os valores do arquivo 'valores.txt' e os retorna como uma lista de inteiros."""
    try:
        with open("valores.txt", "r") as arquivo:
            valores = [int(linha.strip()) for linha in arquivo]
        return valores
    except FileNotFoundError:
        print("arquivo 'valores.txt' não encontrado.")
        return None

if __name__ == "__main__":
    valores = ler_valores()
    if valores:

        # medindo o tempo de execução
        inicio = time.time()
        etapas = [0]  # contador de etapas
        profundidade_max = 2 * math.floor(math.log2(len(valores)))  # calcula a profundidade máxima
        introsort(valores, 0, len(valores) - 1, profundidade_max, etapas)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas[0]}")