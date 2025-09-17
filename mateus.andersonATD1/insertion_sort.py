def insertion_sort_crescente(arr):
    print("Insertion Sort - Ordem Crescente")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move os elementos maiores que key para a direita
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Inserção do elemento key na posição correta
        arr[j + 1] = key
        
        # Estado do vetor após cada inserção
        print(f"Após inserção do elemento na posição {i} ({key}): {arr}")
    print("Resultado final:", arr)
    print()


# Vetores para teste
melhor_caso = [1, 10, 13, 14, 29, 37]
caso_medio = [29, 10, 14, 37, 13, 1]
pior_caso = [37, 29, 14, 13, 10, 1]

# Executando para cada vetor
print("Melhor Caso:")
insertion_sort_crescente(melhor_caso[:])  # Usando cópia para não alterar o original

print("Caso Médio:")
insertion_sort_crescente(caso_medio[:])

print("Pior Caso:")
insertion_sort_crescente(pior_caso[:])
