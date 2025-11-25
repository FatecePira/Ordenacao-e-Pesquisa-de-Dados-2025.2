from time import sleep

def bubble_sort(lista):
    n = len(lista)
    print(f"Vetor inicial: {lista}\n")
    
    for i in range(n):
        trocou = False
        print(f"--- Passada {i+1} ---")
        for j in range(0, n-i-1):
            print(f"Comparando {lista[j]} e {lista[j+1]}...")
            if lista[j] < lista[j+1]:
                print(f"   >> Trocou {lista[j]} com {lista[j+1]}")
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
            else:
                print("   >> Não trocou")
            print(f"   Estado atual: {lista}")
        if not trocou:
            print("Nenhuma troca nesta passada, vetor já está ordenado.\n")
            break
        print(f"Após a passada {i+1}: {lista}\n")
    
    print(f"Vetor final ordenado: {lista}\n")
    print("="*50, "\n")


# Vetores
melhor = [1, 10, 13, 14, 29, 37]
medio  = [29, 10, 14, 37, 13, 1]
pior   = [37, 29, 14, 13, 10, 1]

print(">>> MELHOR CASO")
bubble_sort(melhor)
sleep(5)
print(">>> MÉDIO CASO")
bubble_sort(medio)
sleep(5)
print(">>> PIOR CASO")
bubble_sort(pior)
