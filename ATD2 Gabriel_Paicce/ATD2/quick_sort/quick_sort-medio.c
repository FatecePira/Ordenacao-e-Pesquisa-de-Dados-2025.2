#include <stdio.h>

int comparacoes = 0; // Contador global de comparações

void imprimirVetor(int *V, int N) {
    for (int i = 0; i < N; i++) {
        printf("%d ", V[i]);
    }
    printf("\n");
}

// Função para trocar dois elementos
void trocar(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Função de partição (usa o último elemento como pivô)
int particionar(int *V, int inicio, int fim) {
    int pivo = V[fim];
    int i = inicio - 1;
    printf("Particionando de %d até %d (pivô = %d)\n", inicio, fim, pivo);

    for (int j = inicio; j < fim; j++) {
        comparacoes++;
        printf("  Comparando V[%d]=%d com pivô %d\n", j, V[j], pivo);
        if (V[j] <= pivo) {
            i++;
            printf("  -> Troca: V[%d]=%d <-> V[%d]=%d\n", i, V[i], j, V[j]);
            trocar(&V[i], &V[j]);
        } else {
            printf("  -> Nenhuma troca\n");
        }
    }

    // Coloca o pivô na posição correta
    printf("  Coloca o pivô na posição correta: V[%d]=%d <-> V[%d]=%d\n", i + 1, V[i + 1], fim, V[fim]);
    trocar(&V[i + 1], &V[fim]);

    printf("  Vetor após partição: ");
    imprimirVetor(V, fim + 1);
    printf("\n");

    return i + 1; // Retorna o índice do pivô
}

// Função recursiva de Quick Sort
void quickSort(int *V, int inicio, int fim) {
    if (inicio < fim) {
        int pivo = particionar(V, inicio, fim);

        printf("--> Chamando QuickSort à esquerda (%d até %d)\n\n", inicio, pivo - 1);
        quickSort(V, inicio, pivo - 1);

        printf("--> Chamando QuickSort à direita (%d até %d)\n\n", pivo + 1, fim);
        quickSort(V, pivo + 1, fim);
    }
}

int main() {
    int vetor[] = {29, 10, 14, 37, 13, 1};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor original:\n");
    imprimirVetor(vetor, tamanho);
    printf("\n");

    quickSort(vetor, 0, tamanho - 1);

    printf("Vetor ordenado (crescente):\n");
    imprimirVetor(vetor, tamanho);
    printf("\nNúmero total de comparações: %d\n", comparacoes);

    return 0;
}
