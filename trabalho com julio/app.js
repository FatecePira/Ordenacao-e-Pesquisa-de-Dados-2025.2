//melhor caso
var melhorCaso = [1, 10, 13, 14, 29, 37];
var tamanhoMelhorCaso = melhorCaso.length;
console.log('Melhor caso antes do algoritimo de ordenação: ' + melhorCaso);
insertionSort(melhorCaso, tamanhoMelhorCaso);
console.log('Melhor caso depois do algoritimo insertion sort: ' + melhorCaso);
melhorCaso = [1, 10, 13, 14, 29, 37];
bubbleSort(melhorCaso, tamanhoMelhorCaso);
console.log('Melhor caso depois do algoritimo bubble sort: ' + melhorCaso);

//caso medio
var casoMedio = [29, 10, 14, 37, 13, 1];
var tamanhoCasoMedio = casoMedio.length;
console.log('Caso medio antes do algoritimo de ordenação: ' + casoMedio);
insertionSort(casoMedio, tamanhoCasoMedio);
console.log('Caso medio depois do algoritimo insertion sort: ' + casoMedio);
bubbleSort(casoMedio, tamanhoCasoMedio);
console.log('Caso medio depois do algoritimo bubble sort decrescente: ' + casoMedio);

//pior caso
var piorCaso = [29, 10, 14, 37, 13, 1];
var tamanhoPiorCaso = piorCaso.length;
console.log('Pior caso antes do algoritimo de ordenação: ' + piorCaso);
insertionSort(piorCaso, tamanhoPiorCaso);
console.log('Pior caso depois do algoritimo insertion sort: ' + piorCaso);
bubbleSort(piorCaso, tamanhoPiorCaso);
console.log('Pior caso depois do algoritimo bubble sort decrescente: ' + piorCaso);

//Isertion sort Crescente
function insertionSort(arr, n) {
    console.log('insertion sort crescente - começo')
    let i, j, aux;
    for (i = 1; i < n; i++) {
        aux = arr[i];
        console.log('i:'+i+', j:'+j+', auxiliar:'+aux);
        for (j = i; j  > 0 && aux < arr[j - 1]; j--) {
            arr[j] = arr[j - 1];
        }
        arr[j] = aux;
        console.log('i:'+i+', j:'+j+', auxiliar:'+aux);

    }
    return arr;
}
//Bubble sort Decrescente
function bubbleSort(arr,n){
    console.log('bubble sort decrescente - começo')
    let i,j,aux;
    for(i = n-1; i>=1;i--){
        for(j=0;j<i;j++){
            if(arr[j]<arr[j+1]){
                aux = arr[j];
                arr[j] = arr[j+1];
                console.log('i:'+i+', j:'+j+', auxiliar:'+aux);
                arr[j+1] = aux;
                console.log('i:'+i+', j:'+j+', auxiliar:'+aux);
            }
        }
    }
    return arr;
}