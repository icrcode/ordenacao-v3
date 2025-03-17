import subprocess
import time
import random
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Configurar OpenTelemetry
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)

# Lista de algoritmos disponíveis
ALGORITMOS = [
    "bubble_sort.py",
    "heap_sort.py",
    "insertion_sort.py",
    "intro_sort.py",
    "merge_sort.py",
    "quick_sort.py",
    "selection_sort.py",
    "tim_sort.py",
]

def escolher_quantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de valores a serem gerados: "))
            if quantidade > 0:
                return quantidade
            print("A quantidade deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def gerar_lista(quantidade, tipo):
    if tipo == "aleatorio":
        return [random.randint(0, 1000) for _ in range(quantidade)]
    elif tipo == "meio_ordenado":
        lista = list(range(quantidade))
        for _ in range(quantidade // 5):
            idx1, idx2 = random.randint(0, quantidade - 1), random.randint(0, quantidade - 1)
            lista[idx1], lista[idx2] = lista[idx2], lista[idx1]
        return lista

def salvar_dados(dados, arquivo="valores.txt"):
    with open(arquivo, "w") as f:
        f.write("\n".join(map(str, dados)))

def executar_ordenacao(nome_script):
    with tracer.start_as_current_span(f"Execução {nome_script}"):
        inicio = time.time()
        resultado = subprocess.run(["python", nome_script], capture_output=True, text=True)
        fim = time.time()
        tempo_execucao = fim - inicio
        
        saida = resultado.stdout.strip().split("\n")
        etapas = int(saida[-1].split(": ")[1])  
    
    return tempo_execucao, etapas

def main():
    quantidade = escolher_quantidade()

    escolha = input("Escolha o tipo de dados:\n1 - Completamente aleatórios\n2 - Meio ordenados\nDigite a opção desejada: ")
    tipo_dados = "aleatorio" if escolha == "1" else "meio_ordenado"
    
    print(f"Gerando {tipo_dados.replace('_', ' ')}...")
    dados = gerar_lista(quantidade, tipo_dados)
    salvar_dados(dados)
    
    resultados = []
    for script in ALGORITMOS:
        print(f"Executando {script}...")
        tempo, etapas = executar_ordenacao(script)
        resultados.append((script, tempo, etapas))
    
    print("\nResultados ordenados por tempo de execução:")
    for script, tempo, etapas in sorted(resultados, key=lambda x: x[1]):
        print(f"{script}: {tempo:.6f} segundos")
    
    print("\nResultados ordenados por número de etapas:")
    for script, tempo, etapas in sorted(resultados, key=lambda x: x[2]):
        print(f"{script}: {etapas} etapas")
    
    melhor_algoritmo = min(resultados, key=lambda x: x[2])
    print(f"\nMelhor algoritmo: {melhor_algoritmo[0]} ({melhor_algoritmo[2]} etapas)")

if __name__ == "__main__":
    main()
