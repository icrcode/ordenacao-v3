import subprocess
import time

def executar_ordenacao(nome_script):
    inicio = time.time()
    resultado = subprocess.run(
        ["python", nome_script], 
        capture_output=True, 
        text=True
    )
    fim = time.time()
    tempo_execucao = fim - inicio

    saida = resultado.stdout.strip().split("\n")
    etapas = int(saida[-1].split(": ")[1])  

    return tempo_execucao, etapas

def main():

    print("gerando valores aleatórios...")
    subprocess.run(["python", "gerador_aleatorio.py"])

    scripts = [
        "bubble_sort.py",
        "heap_sort.py",
        "insertion_sort.py",
        "intro_sort.py",
        "merge_sort.py",
        "quick_sort.py",
        "selection_sort.py",
        "tim_sort.py"
    ]

    resultados = []
    for script in scripts:
        print(f"executando {script}...")
        tempo, etapas = executar_ordenacao(script)
        resultados.append((script, tempo, etapas))

    print("\ntempos de execução (do menor para o maior):")
    resultados_ordenados_tempo = sorted(resultados, key=lambda x: x[1])
    for script, tempo, etapas in resultados_ordenados_tempo:
        print(f"{script}: {tempo:.6f} segundos")

    print("\nnúmero de etapas de todos os algoritmos:")
    for script, tempo, etapas in resultados:
        print(f"{script}: {etapas} etapas")

    menor_etapas = min(resultados, key=lambda x: x[2])
    print(f"\nalgoritmo com menor número de etapas: {menor_etapas[0]} ({menor_etapas[2]} etapas)")

if __name__ == "__main__":
    main()