#include <stdio.h>

void bubbleSortDesc(int v[], int n) {
    int i, j, aux;

    for (i = n - 1; i >= 1; i--) {
        for (j = 0; j < i; j++) {
            printf("Comparando v[%d]=%d com v[%d]=%d\n", j, v[j], j + 1, v[j + 1]);

            // Para ordem decrescente, inverte o sinal
            if (v[j] < v[j + 1]) {
                printf(" -> TROCA %d <-> %d\n", v[j], v[j + 1]);
                aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
            } else {
                printf(" -> NENHUMA troca\n");
            }
        }

        // Mostra vetor após cada "passada"
        printf("Vetor apos passo %d: ", n - i);
        for (int k = 0; k < n; k++) {
            printf("%d ", v[k]);
        }
        printf("\n\n");
    }
}

int main() {
    int v[] = {1, 10, 13, 14, 29, 37};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Vetor inicial: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    printf("\n\n");

    bubbleSortDesc(v, n);

    printf("Vetor final (decrescente): ");
    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");

    return 0;
}
