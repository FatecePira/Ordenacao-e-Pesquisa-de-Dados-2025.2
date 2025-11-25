
# QUICK SORT - ORDEM DECRESCENTE


def quick_sort(arr, inicio, fim, depth=0):
    indent = "  " * depth

    if inicio < fim:
        p = particiona(arr, inicio, fim, depth)
        quick_sort(arr, inicio, p - 1, depth + 1)
        quick_sort(arr, p + 1, fim, depth + 1)


def particiona(arr, inicio, fim, depth):
    indent = "  " * depth
    pivo = arr[fim]

    print(f"{indent}Particionando {arr[inicio:fim+1]} com pivo {pivo}")

    i = inicio - 1

    for j in range(inicio, fim):
        print(f"{indent}Comparando {arr[j]} com pivo {pivo}")
        if arr[j] > pivo:  # ORDEM DECRESCENTE
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"{indent}Troca -> {arr}")

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    print(f"{indent}Movendo pivo -> {arr}")

    return i + 1


# Teste com vetores
melhor = [1, 10, 13, 14, 29, 37]
medio = [29, 10, 14, 37, 13, 1]
pior = [37, 29, 14, 13, 10, 1]

print("\n QUICK SORT (DECRESCENTE)")
for vetor in [melhor, medio, pior]:
    print("\nVetor inicial:", vetor)
    arr_copy = vetor.copy()
    quick_sort(arr_copy, 0, len(arr_copy) - 1)
    print("Resultado final:", arr_copy)

# Gabriel Miranda de Sousa
# Gustavo de Oliveira Moraes
