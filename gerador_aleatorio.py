import random

def gerar_numeros_aleatorios(quantidade, limite_inferior=0, limite_superior=100):
    """
    gera uma lista de números aleatórios.
    
    :param quantidade: Número de valores a serem gerados.
    :param limite_inferior: Valor mínimo (inclusive).
    :param limite_superior: Valor máximo (inclusive).
    :return: Lista de números aleatórios.
    """
    return [random.randint(limite_inferior, limite_superior) for _ in range(quantidade)]

def escrever_no_arquivo(valores, nome_arquivo="valores.txt"):
    """
    escreve os valores em um arquivo de texto.hon
    
    :param valores: Lista de valores a serem escritos.
    :param nome_arquivo: Nome do arquivo de saída.
    """
    with open(nome_arquivo, "w") as arquivo:
        for valor in valores:
            arquivo.write(f"{valor}\n")

if __name__ == "__main__":
    # solicita ao usuário a quantidade de números a serem gerados
    quantidade = int(input("quantos números aleatórios deseja gerar? "))
    
    # gera os números aleatórios
    valores = gerar_numeros_aleatorios(quantidade)
    
    # escreve os números no arquivo
    escrever_no_arquivo(valores)
    
    print(f"{quantidade} números aleatórios foram gerados e salvos em 'extra/valores.txt'.")