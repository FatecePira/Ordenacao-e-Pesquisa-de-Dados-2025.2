# ============================
# MERGE SORT (ordem crescente)
# ============================

def merge_sort(arr, depth=0):
    indent = "  " * depth

    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]

    print(f"{indent}Dividindo: {arr} → {esquerda} | {direita}")

    # Recursão
    esquerda = merge_sort(esquerda, depth + 1)
    direita = merge_sort(direita, depth + 1)

    # Fusão
    i = j = 0
    resultado = []

    print(f"{indent}Fundindo: {esquerda} + {direita}")

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            print(f"{indent}Inserção: {esquerda[i]}")
            resultado.append(esquerda[i])
            i += 1
        else:
            print(f"{indent}Inserção: {direita[j]}")
            resultado.append(direita[j])
            j += 1

    # Inserindo restante
    while i < len(esquerda):
        print(f"{indent}Inserção restante: {esquerda[i]}")
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        print(f"{indent}Inserção restante: {direita[j]}")
        resultado.append(direita[j])
        j += 1

    print(f"{indent}Resultado parcial: {resultado}")
    return resultado


# =======================================
# QUICK SORT (ordem decrescente)
# =======================================

def quick_sort(arr, inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1

    if inicio < fim:
        p = particiona(arr, inicio, fim)
        quick_sort(arr, inicio, p - 1)
        quick_sort(arr, p + 1, fim)


def particiona(arr, inicio, fim):
    pivo = arr[fim]
    i = inicio - 1

    print(f"\nParticionando (pivô = {pivo}): {arr[inicio:fim+1]}")

    for j in range(inicio, fim):
        # Como é DECRESCENTE, inverte a condição
        if arr[j] >= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"TROCA: {arr}")

    arr[i+1], arr[fim] = arr[fim], arr[i+1]
    print(f"TROCA pivô: {arr}")

    return i + 1


# ==========================================
# Execução pedida pela atividade
# ==========================================

melhor = [1, 10, 13, 14, 29, 37]
medio  = [29, 10, 14, 37, 13, 1]
pior   = [37, 29, 14, 13, 10, 1]

conjuntos = [("Melhor Caso", melhor),
             ("Caso Médio", medio),
             ("Pior Caso", pior)]

print("\n\n============================")
print(" MERGE SORT (ordem crescente)")
print("============================\n")

for nome, vetor in conjuntos:
    print(f"\n--- {nome} ---")
    resultado = merge_sort(vetor.copy())
    print(f"→ Resultado final: {resultado}\n")


print("\n\n============================")
print(" QUICK SORT (ordem decrescente)")
print("============================\n")

for nome, vetor in conjuntos:
    print(f"\n--- {nome} ---")
    v = vetor.copy()
    quick_sort(v)
    print(f"→ Resultado final: {v}\n")
