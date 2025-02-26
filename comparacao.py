import subprocess
import time
import random

def gerar_aleatorio(quantidade):
    return [random.randint(0, 1000) for _ in range(quantidade)]

def gerar_meio_ordenado(quantidade):
    lista = [i for i in range(quantidade)]

    for _ in range(quantidade // 5):
        idx1, idx2 = random.randint(0, quantidade - 1), random.randint(0, quantidade - 1)
        lista[idx1], lista[idx2] = lista[idx2], lista[idx1]
    return lista

def salvar_dados(dados):
    with open("valores.txt", "w") as arquivo:
        for valor in dados:
            arquivo.write(f"{valor}\n")

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
    print("escolha o tipo de dados:")
    print("1 - completamente aleatórios")
    print("2 - meio ordenados")
    escolha = input("digite o número da opção desejada: ")

    quantidade = 100  
    if escolha == "1":
        print("gerando dados completamente aleatórios...")
        dados = gerar_aleatorio(quantidade)
    elif escolha == "2":
        print("gerando dados meio ordenados...")
        dados = gerar_meio_ordenado(quantidade)
    else:
        print("opção inválida. gerando dados completamente aleatórios por padrão.")
        dados = gerar_aleatorio(quantidade)

    salvar_dados(dados)

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

    print("\nnúmero de etapas (do menor para o maior):")
    resultados_ordenados_etapas = sorted(resultados, key=lambda x: x[2])
    for script, tempo, etapas in resultados_ordenados_etapas:
        print(f"{script}: {etapas} etapas")

    menor_etapas = min(resultados, key=lambda x: x[2])
    print(f"\nalgoritmo com menor número de etapas: {menor_etapas[0]} ({menor_etapas[2]} etapas)")

if __name__ == "__main__":
    main()