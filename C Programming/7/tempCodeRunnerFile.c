#include<stdio.h>

int main(){
    int m, n;
    printf("Enter the no: ");
    scanf("%d", &n);
    printf("Enter the no: of row: ")
    scanf("%d", &m);

    int marks[3][5];
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){jhgjb
            printf("Enter the marks of student %d in subject %d\n", i+1, j+1);
            scanf("%d", &marks[i][j]);
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            printf("The marks of student %d in subject %d is: %d\n", i+1, j+1, marks[i][j]);
        }
    }

    return 0;
}