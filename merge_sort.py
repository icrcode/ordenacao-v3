import time

def merge_sort(arr, etapas=[0]):
    if len(arr) > 1:
        # divide o array ao meio
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        # recursivamente ordena as duas metades
        merge_sort(esquerda, etapas)
        merge_sort(direita, etapas)

        # combina as metades ordenadas
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1
            etapas[0] += 1  # conta cada comparação

        # copia os elementos restantes de esquerda (se houver)
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1
            etapas[0] += 1  # conta cada cópia

        # copia os elementos restantes de direita (se houver)
        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1
            etapas[0] += 1  # conta cada cópia

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
        etapas = merge_sort(valores)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")