import time

def insertion_sort(arr):
    etapas = 0  # contador de etapas (comparações e trocas)
    for i in range(1, len(arr)):
        chave = arr[i]  # elemento atual a ser inserido na posição correta
        j = i - 1

        # move os elementos maiores que a chave para a direita
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
            etapas += 1  # conta cada troca
        etapas += 1  # conta cada comparação

        # insere a chave na posição correta
        arr[j + 1] = chave

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
        etapas = insertion_sort(valores)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")