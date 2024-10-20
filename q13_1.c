#include <stdio.h>
#include <stdbool.h>

bool printDiamond(int rows) {
    if (rows % 2 == 0) {
        printf("Error: Number of rows must be odd.\n");
        return false;
    }

    int n = rows / 2;  
    
    
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j < n - i; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    
    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < n - i; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }
    
    return true;
}

int main() {
    int rows;
    printf("Enter number of rows: ");
    scanf("%d", &rows);

    bool result = printDiamond(rows);
    if (result) {
        printf("Diamond pattern printed successfully.\n");
    }

    return 0;
}
