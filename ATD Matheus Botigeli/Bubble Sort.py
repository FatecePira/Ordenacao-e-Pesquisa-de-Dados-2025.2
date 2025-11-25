import time
v = [37, 29, 14, 13, 10, 1]

def bubble_sort(v):
    size = len(v)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if v[j] < v[j + 1]:
                temp = v[j]
                v[j] = v[j + 1]
                v[j + 1] = temp
                print(f"Troca {v[j+1]} com {v[j]} e fica -> {v}")

# mede o tempo
inicio = time.time()
bubble_sort(v)
fim = time.time()

print(v)
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
print("Lista final:", v)