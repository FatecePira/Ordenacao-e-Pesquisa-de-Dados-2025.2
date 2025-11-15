# Quicksort (ordenação em forma crescente)
import time

melhor_caso = [1,10,13,14,20,37]
caso_medio = [29,10,14,37,13,1]
pior_caso = [37,29,14,13,10,1]

l = 0
r = 5

def trocar_elementos(array, a, b):
    aux = array[a]
    array[a] = array[b]
    array[b] = aux

def partition(array, l, r):

    # Seleciona l como pivo
    pivo = array[l]
    j = l
    print(f"\nIndice [{l}] ao [{r}] / pivo = {pivo}")
    
    for i in range(l+1, r+1):
        if array[i] <= array[l]:
            j = j + 1
            trocar_elementos(array, i, j)

    trocar_elementos(array, l, j)
    print(f"Pivo {pivo} colocado na posição [{j}]")
    print(f"Array após partition: {array} \n")
    return j #retorna j como pivo

def quick_sort(array, l, r):
    
    if l < r:
        pivo = partition(array, l, r)
        quick_sort(array, l, pivo-1)
        quick_sort(array, pivo +1, r)

def main():
    print ("***APLICAÇÃO DO QUICK_SORT PARA ORDENAÇÃO CRESCENTE***\n")
    print("***ORDENANDO MELHOR CASO [1,10,13,14,20,37]***\n ")
    quick_sort(melhor_caso, l ,r)
    print(f"MELHOR CASO ORDENADO DE FORMA CRESCENTE: {melhor_caso} \n\n")
    time.sleep(10)

    print("----------------------------------------- \n\n ***ORDENANDO CASO MÉDIO [29,10,14,37,13,1]*** \n")
    quick_sort(caso_medio, l ,r)
    print(f"CASO MÉDIO ORDENADO DE FORMA CRESCENTE: {caso_medio} \n\n")
    time.sleep(10)

    print("\n ----------------------------------------- \n\n ***ORDENANDO PIOR CASO [37,29,14,13,10,1]*** \n")
    quick_sort(pior_caso, l ,r)
    print(f"PIOR CASO ORDENADO DE FORMA CRESCENTE: {pior_caso} \n\n ***FIM*** \n")
    time.sleep(10)
    
main()