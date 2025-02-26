import time

def heapify(arr, n, i, etapas):
    """
    transforma um subárvore enraizada no índice 'i' em um heap máximo.
    
    :param arr: array a ser ordenado.
    :param n: tamanho do heap.
    :param i: índice da raiz da subárvore.
    :param etapas: contador de etapas (comparações e trocas).
    """
    maior = i  # inicializa o maior como raiz
    esquerda = 2 * i + 1  # índice do filho esquerdo
    direita = 2 * i + 2  # índice do filho direito

    # verifica se o filho esquerdo é maior que a raiz
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda
    etapas[0] += 1  # conta cada comparação

    # verifica se o filho direito é maior que o maior atual
    if direita < n and arr[direita] > arr[maior]:
        maior = direita
    etapas[0] += 1  # conta cada comparação

    # se o maior não for a raiz, troca e faz heapify no subárvore afetado
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        etapas[0] += 1  # conta cada troca
        heapify(arr, n, maior, etapas)

def heap_sort(arr):
    """
    ordena o array usando o algoritmo Heap Sort.
    
    :param arr: array a ser ordenado.
    :return: número total de etapas (comparações e trocas).
    """
    n = len(arr)
    etapas = [0]  # contador de etapas

    # constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, etapas)

    # extrai elementos do heap um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # troca o elemento raiz (maior) com o último
        etapas[0] += 1  # conta cada troca
        heapify(arr, i, 0, etapas)  # faz heapify no heap reduzido

    return etapas[0]

def ler_valores():
    """
    lê os valores do arquivo 'valores.txt' e os retorna como uma lista de inteiros.
    
    :return: lista de valores lidos ou none se o arquivo não for encontrado.
    """
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
        
        inicio = time.time()
        etapas = heap_sort(valores)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")