#include <stdio.h>

// Função para mesclar duas partes do vetor em ordem DECRESCENTE
void mergeDesc(int v[], int inicio, int meio, int fim) {
    int n1 = meio - inicio + 1;
    int n2 = fim - meio;

    int L[n1], R[n2];

    // Copia dados para vetores temporários L[] e R[]
    for (int i = 0; i < n1; i++)
        L[i] = v[inicio + i];
    for (int j = 0; j < n2; j++)
        R[j] = v[meio + 1 + j];

    int i = 0, j = 0, k = inicio;

    printf("Mesclando partes [%d..%d] e [%d..%d]\n", inicio, meio, meio + 1, fim);

    // Mescla os vetores temporários de volta ao original (decrescente)
    while (i < n1 && j < n2) {
        printf("Comparando L[%d]=%d e R[%d]=%d\n", i, L[i], j, R[j]);
        if (L[i] >= R[j]) {
            printf("  -> Escolhe %d (de L)\n", L[i]);
            v[k++] = L[i++];
        } else {
            printf("  -> Escolhe %d (de R)\n", R[j]);
            v[k++] = R[j++];
        }
    }

    // Copia os elementos restantes de L[], se houver
    while (i < n1) {
        v[k++] = L[i++];
    }

    // Copia os elementos restantes de R[], se houver
    while (j < n2) {
        v[k++] = R[j++];
    }

    // Mostra vetor após a mesclagem desta parte
    printf("Vetor apos mesclagem [%d..%d]: ", inicio, fim);
    for (int x = inicio; x <= fim; x++) printf("%d ", v[x]);
    printf("\n\n");
}

// Função recursiva de Merge Sort (decrescente)
void mergeSortDesc(int v[], int inicio, int fim) {
    if (inicio < fim) {
        int meio = inicio + (fim - inicio) / 2;

        // Divide o vetor em duas metades
        mergeSortDesc(v, inicio, meio);
        mergeSortDesc(v, meio + 1, fim);

        // Mescla as duas metades ordenadas
        mergeDesc(v, inicio, meio, fim);
    }
}

int main() {
    int v[] = {37, 29, 14, 13, 10, 1};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Vetor inicial: ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);
    printf("\n\n");

    mergeSortDesc(v, 0, n - 1);

    printf("Vetor final (decrescente): ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);
    printf("\n");

    return 0;
}