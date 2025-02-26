import time

# tamanho mínimo de um "run" (bloco)
MIN_MERGE = 32

def insertion_sort(arr, esquerda, direita, etapas):
    """ordena o array usando Insertion Sort."""
    for i in range(esquerda + 1, direita + 1):
        j = i
        while j > esquerda and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            etapas[0] += 1  # conta cada troca
        etapas[0] += 1  # conta cada comparação

def merge(arr, esquerda, meio, direita, etapas):
    """combina dois runs ordenados."""
    len1, len2 = meio - esquerda + 1, direita - meio
    esquerda_arr = arr[esquerda:meio + 1]
    direita_arr = arr[meio + 1:direita + 1]

    i = j = 0
    k = esquerda

    while i < len1 and j < len2:
        if esquerda_arr[i] <= direita_arr[j]:
            arr[k] = esquerda_arr[i]
            i += 1
        else:
            arr[k] = direita_arr[j]
            j += 1
        k += 1
        etapas[0] += 1  # conta cada comparação

    while i < len1:
        arr[k] = esquerda_arr[i]
        i += 1
        k += 1
        etapas[0] += 1  # conta cada cópia

    while j < len2:
        arr[k] = direita_arr[j]
        j += 1
        k += 1
        etapas[0] += 1  # conta cada cópia

def tim_sort(arr, etapas=[0]):
    """implementação do tim sort."""
    n = len(arr)

    # ordena pequenos blocos com Insertion Sort
    for esquerda in range(0, n, MIN_MERGE):
        direita = min(esquerda + MIN_MERGE - 1, n - 1)
        insertion_sort(arr, esquerda, direita, etapas)

    # combina os blocos com merge sort
    tamanho = MIN_MERGE
    while tamanho < n:
        for esquerda in range(0, n, 2 * tamanho):
            meio = min(n - 1, esquerda + tamanho - 1)
            direita = min(n - 1, esquerda + 2 * tamanho - 1)
            if meio < direita:
                merge(arr, esquerda, meio, direita, etapas)
        tamanho *= 2

    return etapas[0]

def ler_valores():
    try:
        with open("valores.txt", "r") as arquivo:
            valores = [int(linha.strip()) for linha in arquivo]
        return valores
    except FileNotFoundError:
        print("como eu esqueci disso...")
        return None

if __name__ == "__main__":
    valores = ler_valores()
    if valores:

        # medindo o tempo de execução
        inicio = time.time()
        etapas = tim_sort(valores)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")