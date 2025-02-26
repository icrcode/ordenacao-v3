import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def gerar_aleatorio(quantidade):
    return [random.randint(1, 100) for _ in range(quantidade)]

def gerar_meio_ordenado(quantidade):
    lista = [i for i in range(1, quantidade + 1)]
    for _ in range(quantidade // 5):
        idx1, idx2 = random.randint(0, quantidade - 1), random.randint(0, quantidade - 1)
        lista[idx1], lista[idx2] = lista[idx2], lista[idx1]
    return lista

def bubble_sort(arr, atualizar_visualizacao):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                atualizar_visualizacao(arr)
                time.sleep(0.01)

def insertion_sort(arr, atualizar_visualizacao):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
            atualizar_visualizacao(arr)
            time.sleep(0.01)
        arr[j + 1] = chave
        atualizar_visualizacao(arr)

def atualizar_visualizacao(arr):
    ax.clear()
    ax.bar(range(len(arr)), arr, color='skyblue')
    ax.set_title("Ordenação em Tempo Real")
    canvas.draw()

def executar_ordenacao(algoritmo, arr):
    if algoritmo == "Bubble Sort":
        bubble_sort(arr, atualizar_visualizacao)
    elif algoritmo == "Insertion Sort":
        insertion_sort(arr, atualizar_visualizacao)
    messagebox.showinfo("Concluído", f"{algoritmo} finalizado!")

def iniciar_ordenacao():
    quantidade = int(entrada_quantidade.get())
    tipo_dados = combo_tipo_dados.get()
    algoritmo = combo_algoritmo.get()

    if tipo_dados == "Completamente Aleatórios":
        dados = gerar_aleatorio(quantidade)
    else:
        dados = gerar_meio_ordenado(quantidade)

    ax.clear()
    ax.bar(range(len(dados)), dados, color='skyblue')
    ax.set_title("Ordenação em Tempo Real")
    canvas.draw()

    threading.Thread(target=executar_ordenacao, args=(algoritmo, dados)).start()

root = tk.Tk()
root.title("Comparador Dinâmico de Algoritmos de Ordenação")

frame_entrada = ttk.Frame(root)
frame_entrada.pack(padx=10, pady=10)

ttk.Label(frame_entrada, text="Quantidade de valores:").grid(row=0, column=0, padx=5, pady=5)
entrada_quantidade = ttk.Entry(frame_entrada)
entrada_quantidade.grid(row=0, column=1, padx=5, pady=5)
entrada_quantidade.insert(0, "50")  # Valor padrão

ttk.Label(frame_entrada, text="Tipo de dados:").grid(row=1, column=0, padx=5, pady=5)
combo_tipo_dados = ttk.Combobox(frame_entrada, values=["Completamente Aleatórios", "Meio Ordenados"])
combo_tipo_dados.grid(row=1, column=1, padx=5, pady=5)
combo_tipo_dados.current(0)

ttk.Label(frame_entrada, text="Algoritmo:").grid(row=2, column=0, padx=5, pady=5)
combo_algoritmo = ttk.Combobox(frame_entrada, values=["Bubble Sort", "Insertion Sort"])
combo_algoritmo.grid(row=2, column=1, padx=5, pady=5)
combo_algoritmo.current(0)

ttk.Button(frame_entrada, text="Iniciar Ordenação", command=iniciar_ordenacao).grid(row=3, column=0, columnspan=2, pady=10)

fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=10, pady=10)

root.mainloop()