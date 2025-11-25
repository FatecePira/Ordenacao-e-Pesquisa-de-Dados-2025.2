
# MERGE SORT - ORDEM CRESCENTE


def merge_sort(arr, depth=0):
    indent = "  " * depth  # identação para visualizar recursão

    print(f"{indent}Dividindo: {arr}")

    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        # Chamada recursiva nas metades
        merge_sort(esquerda, depth + 1)
        merge_sort(direita, depth + 1)

        i = j = k = 0

        print(f"{indent}Intercalando {esquerda} e {direita}")

        # Intercalação das metades
        while i < len(esquerda) and j < len(direita):
            print(f"{indent}Comparando {esquerda[i]} e {direita[j]}")
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            print(f"{indent}Estado parcial: {arr}")
            k += 1

        # Copia o restante da esquerda
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1
            print(f"{indent}Restante esquerda -> {arr}")

        # Copia o restante da direita
        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1
            print(f"{indent}Restante direita -> {arr}")

    print(f"{indent}Retornando: {arr}")
    return arr


# Teste com os 3 vetores
melhor = [1, 10, 13, 14, 29, 37]
medio = [29, 10, 14, 37, 13, 1]
pior = [37, 29, 14, 13, 10, 1]

print("\n MERGE SORT (CRESCENTE)")
for vetor in [melhor, medio, pior]:
    print("\nVetor inicial:", vetor)
    merge_sort(vetor.copy())

# Gabriel Miranda de Sousa
# Gustavo de Oliveira Moraes
