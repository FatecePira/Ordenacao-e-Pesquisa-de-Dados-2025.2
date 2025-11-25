import time 
v = [37, 29, 14, 13, 10, 1]

def selection_sort(v):
    size = len(v)
    for i in range(size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if(v[j] < v[min_idx]):
                min_idx = j
        if(min_idx != i):
            temp = v[i]
            v[i] = v[min_idx]
            v[min_idx] = temp
            print(f"Troca {v[min_idx]} com o {v[i]} e fica -> {v}")
            
# mede o tempo
inicio = time.time()
selection_sort(v)
fim = time.time()

print(v)
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
print("Lista final:", v)