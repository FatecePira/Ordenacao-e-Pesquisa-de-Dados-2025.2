def insertion_sort(arr):

    print(f"\nInsertion Sort (decrescente) - vetor inicial: {arr}")
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < chave:
            print(f"Movendo {arr[j]} para a direita")
            arr[j+1] = arr[j]
            j -= 1
            print("Estado do vetor:", arr)
        arr[j+1] = chave
        print(f"Inserção da chave {chave}: {arr}")
    print("Resultado final:", arr)


melhor = [1, 10, 13, 14, 29, 37]
medio = [29, 10, 14, 37, 13, 1]
pior = [37, 29, 14, 13, 10, 1]

for vetor in [melhor, medio, pior]:
    insertion_sort(vetor.copy())

# Gabriel Miranda de Sousa
# Gustavo de Oliveira Moraes
