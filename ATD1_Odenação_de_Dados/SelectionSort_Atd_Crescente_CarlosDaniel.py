from time import sleep #optei por colocar sleep pois os processos acabam sendo pesados devido a demanda 

def selection_sort(Vetor):
    t = 0
    c = 0
    original = Vetor.copy() #salvando o vetor para mostrar quais os dados que vão ser utilizados
    
    print(f"O Vetor Antes da Troca : {original}")
    n = len(Vetor)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            c += 1 # vai contar quantas comparações foram feitas, para dar mais detalhes e ver se compensa
            if Vetor[j] < Vetor[menor]:
                menor = j
        if menor != i:  # só mostra quando tem troca
            print(f"Troca: {Vetor[i]} <-> {Vetor[menor]}")
            Vetor[i], Vetor[menor] = Vetor[menor], Vetor[i]
            print("Estado atual:", Vetor)
            t += 1
        sleep(2)
    
    print("")
    print("-- Ao todo foram feitas {} trocas neste processo. ".format(t))
    sleep(1)
    print(f"-- E também foram feitas {c} comparações até a ordenação crescente de:\n-- {original} <-por-> {Vetor}")
    sleep(1)
    print("-- Resultado final:", Vetor)
    print('')


# Dados dos vetores pedidos na Atd
melhor = [1, 10, 13, 14, 29, 37]
medio  = [29, 10, 14, 37, 13, 1]
pior   = [37, 29, 14, 13, 10, 1]

# Executando Selection Sort em cada caso para mostrar com clareza quem está sendo executado
for caso, vetor in [("Melhor", melhor), ("Médio", medio), ("Pior", pior)]:
    print('-=' * 30)
    print(f"----- Caso {caso} -----")
    selection_sort(vetor.copy())

print("-=" * 30)
#obs: Mesmo não havendo números para serem trocados o Selection Sort faz comparações, consumindo processos sem nescessidades!!