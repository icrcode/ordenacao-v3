import time

def quick_sort(arr, inicio, fim, etapas=[0]):
    if inicio < fim:
        # particiona o array e obtém o índice do pivô
        pivo_idx = particionar(arr, inicio, fim, etapas)
        
        # ordena recursivamente as duas partições
        quick_sort(arr, inicio, pivo_idx - 1, etapas)
        quick_sort(arr, pivo_idx + 1, fim, etapas)

    return etapas[0]

def particionar(arr, inicio, fim, etapas):
    # escolhe o último elemento como pivô
    pivo = arr[fim]
    i = inicio - 1  # índice do menor elemento

    for j in range(inicio, fim):
        # se o elemento atual é menor ou igual ao pivô
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # troca os elementos
            etapas[0] += 1  # conta cada troca
        etapas[0] += 1  # conta cada comparação

    # coloca o pivô na posição correta
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    etapas[0] += 1  # conta a troca do pivô

    return i + 1  # retorna o índice do pivô

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
        etapas = quick_sort(valores, 0, len(valores) - 1)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")