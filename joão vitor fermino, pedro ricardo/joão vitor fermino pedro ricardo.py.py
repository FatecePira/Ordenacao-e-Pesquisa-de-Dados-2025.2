# Bubble Sort (ordem crescente)
def bubble_sort(arr):
    n = len(arr)
    print(f"\n--- Bubble Sort (Crescente) ---")
    print(f"Vetor inicial: {arr}")
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"Troca: {arr[j]} <-> {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Estado atual: {arr}")
    print(f"Resultado final: {arr}")


# Insertion Sort (ordem decrescente)
def insertion_sort(arr):
    print(f"\n--- Insertion Sort (Decrescente) ---")
    print(f"Vetor inicial: {arr}")
    
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < chave:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Movendo elemento: {arr}")
        arr[j + 1] = chave
        print(f"Inserção da chave {chave}: {arr}")
    print(f"Resultado final: {arr}")


# -------------------------
# Testes com os vetores
# -------------------------

melhor = [1, 10, 13, 14, 29, 37]
medio = [29, 10, 14, 37, 13, 1]
pior  = [37, 29, 14, 13, 10, 1]

# Bubble Sort crescente
for caso, vetor in [("Melhor caso", melhor.copy()), 
                    ("Caso médio", medio.copy()), 
                    ("Pior caso", pior.copy())]:
    print(f"\n### {caso} ###")
    bubble_sort(vetor)

# Insertion Sort decrescente
for caso, vetor in [("Melhor caso", melhor.copy()), 
                    ("Caso médio", medio.copy()), 
                    ("Pior caso", pior.copy())]:
    print(f"\n### {caso} ###")
    insertion_sort(vetor)