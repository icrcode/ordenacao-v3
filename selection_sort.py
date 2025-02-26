import time

def selection_sort(arr):
    n = len(arr)
    etapas = 0  # contador de etapas (comparações e trocas)
    for i in range(n):
        # encontra o índice do menor elemento no restante do array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            etapas += 1  # conta cada comparação

        # troca o elemento atual pelo menor encontrado
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            etapas += 1  # conta cada troca
    return etapas

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
        etapas = selection_sort(valores)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")