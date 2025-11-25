#include <stdio.h>

void imprimirVetor(int *V, int N) {
    for (int i = 0; i < N; i++) {
        printf("%d ", V[i]);
    }
    printf("\n");
}

void selectionSort(int *V, int N) {
    int i, j, menor, troca;
    int comparacoes = 0;

    for (i = 0; i < N - 1; i++) {
        menor = i;
        printf("Passo %d:\n", i + 1);

        for (j = i + 1; j < N; j++) {
            comparacoes++;
            printf(" Comparando V[%d]=%d com V[%d]=%d\n", j, V[j], menor, V[menor]);

            if (V[j] < V[menor]) {
                menor = j;
                printf(" Novo menor encontrado no índice %d (valor %d)\n", menor, V[menor]);
            }
        }

        if (i != menor) {
            printf(" Troca: V[%d]=%d <-> V[%d]=%d\n", i, V[i], menor, V[menor]);
            troca = V[i];
            V[i] = V[menor];
            V[menor] = troca;
        } else {
            printf(" Nenhuma troca necessária\n");
        }

        printf(" Vetor após o passo %d: ", i + 1);
        imprimirVetor(V, N);
        printf("\n");
    }

    printf("Número total de comparações: %d\n", comparacoes);
}

int main() {
    int vetor[] = {1, 10, 13, 14, 29, 37};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor original:\n");
    imprimirVetor(vetor, tamanho);
    printf("\n");

    selectionSort(vetor, tamanho);

    printf("Vetor ordenado:\n");
    imprimirVetor(vetor, tamanho);

    return 0;
}
