import time

def bubble_sort(arr):
    n = len(arr)
    etapas = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            etapas += 1
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
        etapas = bubble_sort(valores)
        fim = time.time()

        print(f"tempo de execução: {fim - inicio:.6f} segundos")
        print(f"número de etapas: {etapas}")