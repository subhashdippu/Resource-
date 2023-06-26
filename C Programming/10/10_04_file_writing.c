#include<stdio.h>

int main(){
    FILE *fptr;
    int number = 45;
    fptr = fopen("generated.txt", "w");
    fprintf(fptr, "The number is %d\n", number); // Here fprintf is used for write in file
    fprintf(fptr, "Thanks for using fprintf", number);
    fclose(fptr);

    return 0;
}