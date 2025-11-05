# MERGE SORT (ordem crescente)
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

# QUICK SORT (ordem decrescente)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        maiores = [x for x in arr[1:] if x >= pivo]
        menores = [x for x in arr[1:] if x < pivo]
        return quick_sort(maiores) + [pivo] + quick_sort(menores)

# VETORES DE TESTE

melhor_caso = [1, 10, 13, 14, 29, 37]
caso_medio = [29, 10, 14, 37, 13, 1]
pior_caso = [37, 29, 14, 13, 10, 1]

# TESTANDO MERGE SORT (Crescente)

print("=== MERGE SORT (Crescente) ===")
for nome, vetor in [("Melhor caso", melhor_caso.copy()),
                    ("Caso médio", caso_medio.copy()),
                    ("Pior caso", pior_caso.copy())]:
    merge_sort(vetor)
    print(f"{nome}: {vetor}")


# TESTANDO QUICK SORT (Decrescente)

print("\n=== QUICK SORT (Decrescente) ===")
for nome, vetor in [("Melhor caso", melhor_caso.copy()),
                    ("Caso médio", caso_medio.copy()),
                    ("Pior caso", pior_caso.copy())]:
    ordenado = quick_sort(vetor)
    print(f"{nome}: {ordenado}")