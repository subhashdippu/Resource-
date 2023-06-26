#include<stdio.h>

int main(){
    FILE *ptr;
    // fgetc demo for reading a file
    ptr = fopen("getcdemo.txt", "r");
    // char c = fgetc(ptr); // This is the function which is used for read the file charactor by charactor
    printf("The value of my character is %c\n", fgetc(ptr));
    printf("The value of my character is %c\n", fgetc(ptr));
    printf("The value of my character is %c\n", fgetc(ptr));
    printf("The value of my character is %c\n", fgetc(ptr));
    printf("The value of my character is %c\n", fgetc(ptr));

    // ptr = fopen("putcdemo.txt", "w");
    // putc('c', ptr); // This is the function which is used for write in the file charactor by charactor
    // putc('c', ptr);
    // putc('c', ptr);
    fclose(ptr);
    return 0;
}