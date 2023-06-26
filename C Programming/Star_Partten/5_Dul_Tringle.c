#include<stdio.h>

int main(){
    int num;
    printf("Enter the no: ");
    scanf("%d", &num);
    for(int i=1; i<=num; i++){
        for(int j=1; j<=(num*2)-1; j++){
            if(j <= (num+1)-i || j>=(num-1)+i){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}