#include <stdio.h>

void printParallelogram(int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        
        for (int j = 0; j < i; j++) {
            printf(" ");
        }
        
        for (int j = 0; j < cols; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int rows, cols;
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    printf("Enter number of columns: ");
    scanf("%d", &cols);

    printParallelogram(rows, cols);

    return 0;
}
