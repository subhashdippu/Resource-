#include<stdio.h>

int main(){
    char s[34];
    int c;
    printf("Enter your name: ");
    gets(s);  // gets is use as a scanf function but in gets we can write sentences gets() reads input until it encounters newline or End Of File
    puts(s);  // puts is use as a printf function but puts() is use only for string 
    printf("Your name is %s", s);
    return 0;
}