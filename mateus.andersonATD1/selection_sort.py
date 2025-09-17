def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        print(f'Seleção do índice {max_idx} como maior inicialmente: {arr}')
        
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
                print(f'Novo índice máximo selecionado: {max_idx} (valor {arr[max_idx]})')
        
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            print(f'Troca: arr[{i}] ({arr[max_idx]}) com arr[{max_idx}] ({arr[i]}) -> {arr}')
        else:
            print(f'Sem troca para posição {i} -> {arr}')
    print(f'Vetor ordenado (decrescente): {arr}\n')

# Vetores para teste
melhor_caso = [1, 10, 13, 14, 29, 37]
caso_medio = [29, 10, 14, 37, 13, 1]
pior_caso = [37, 29, 14, 13, 10, 1]

print("== Melhor Caso ==")
selection_sort_desc(melhor_caso.copy())

print("== Caso Médio ==")
selection_sort_desc(caso_medio.copy())

print("== Pior Caso ==")
selection_sort_desc(pior_caso.copy())
