# Atividade de Ordenação - Relatório Visual em Tabela

def selection_sort(arr, crescente=True, arquivo=None):
    """Selection Sort com registro em tabela"""
    log(f"\n--- Selection Sort ({'Crescente' if crescente else 'Decrescente'}) ---", arquivo)
    log_vetor(arr, "Inicial", arquivo)
    n = len(arr)
    for i in range(n):
        idx_extremo = i
        for j in range(i+1, n):
            if (crescente and arr[j] < arr[idx_extremo]) or (not crescente and arr[j] > arr[idx_extremo]):
                idx_extremo = j
        if idx_extremo != i:
            arr[i], arr[idx_extremo] = arr[idx_extremo], arr[i]
            log_vetor(
                arr, f"Trocando {arr[idx_extremo]} com {arr[i]}", arquivo)
    log_vetor(arr, "Ordenado", arquivo)
    return arr


def insertion_sort(arr, crescente=True, arquivo=None):
    """Insertion Sort com registro em tabela"""
    log(f"\n--- Insertion Sort ({'Crescente' if crescente else 'Decrescente'}) ---", arquivo)
    log_vetor(arr, "Inicial", arquivo)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((crescente and arr[j] > key) or (not crescente and arr[j] < key)):
            arr[j + 1] = arr[j]
            log_vetor(arr, f"Movendo {arr[j]}", arquivo)
            j -= 1
        arr[j + 1] = key
        log_vetor(arr, f"Inserindo {key}", arquivo)
    log_vetor(arr, "Ordenado", arquivo)
    return arr


def log(mensagem, arquivo):
    """Registra mensagem no console e no arquivo"""
    print(mensagem)
    if arquivo:
        arquivo.write(mensagem + "\n")


def log_vetor(arr, acao, arquivo):
    """Imprime o vetor em formato de tabela com índice e valor"""
    indices = ' | '.join(f"{i:>3}" for i in range(len(arr)))
    valores = ' | '.join(f"{v:>3}" for v in arr)
    log(f"{acao}:\nÍndices: {indices}\nValores : {valores}\n", arquivo)

# Conjuntos de Dados

melhor_caso = [1, 10, 13, 14, 29, 37]
caso_medio = [29, 10, 14, 37, 13, 1]
pior_caso = [37, 29, 14, 13, 10, 1]

# Execução 

with open("_ordenacao_tabela", "w") as arquivo:
    for algoritmo, func in zip(
        ["Selection Sort Crescente", "Insertion Sort Decrescente"],
        [selection_sort, insertion_sort]
    ):
        crescente = True if "Crescente" in algoritmo else False
        log(f"\n{'='*50}\n{algoritmo}\n{'='*50}", arquivo)
        for caso, nome in zip([melhor_caso, caso_medio, pior_caso], ["Melhor Caso", "Caso Médio", "Pior Caso"]):
            log(f"\n>>> {nome} <<<", arquivo)
            func(caso.copy(), crescente=crescente, arquivo=arquivo)

print("\nRelatório completo em tabela salvo em 'ordenacao_tabela'")
