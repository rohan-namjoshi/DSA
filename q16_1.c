#include <stdio.h>

void printPattern(int rows) {
    for (int i = 1; i <= rows; i++) {
        for (int j = i; j <= rows; j++) {
            printf("%d", j);
        }
        for (int j = rows - 1; j >= i; j--) {
            printf("%d", rows);
        }
        printf("\n");
    }
}

int main() {
    int rows;
    printf("Enter number of rows: ");
    scanf("%d", &rows);

    printPattern(rows);

    return 0;
}
