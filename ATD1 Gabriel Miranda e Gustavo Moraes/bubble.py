def bubble_sort(arr):  # Função do bubble sort
    n = len(arr)  # Verifica tamanho do vetor
    # Imprime o vetor inicial
    print(f"\nBubble Sort (crescente) - vetor inicial: {arr}")
    for i in range(n-1):  # percorre o vetor
        for j in range(n-1-i):  # compara os elementos adjacentes
            if arr[j] > arr[j+1]:  # verifica se o elemento atual é maior que o próximo
                print(f"Troca: {arr[j]} ↔ {arr[j+1]}")  # imprime a troca
                arr[j], arr[j+1] = arr[j+1], arr[j]  # realiza a troca
                print("Estado do vetor:", arr)  # imprime o vetor pós troca
    print("Resultado final:", arr)  # Imprime o vetor ordenado


melhor = [1, 10, 13, 14, 29, 37]  # Vetor em ordem crescente
medio = [29, 10, 14, 37, 13, 1]  # Vetor em ordem aleatória
pior = [37, 29, 14, 13, 10, 1]  # Vetor em ordem decrescente

for vetor in [melhor, medio, pior]:  # chama o bubble sort para cada vetor
    bubble_sort(vetor.copy())

# Gabriel Miranda de Sousa
# Gustavo de Oliveira Moraes
