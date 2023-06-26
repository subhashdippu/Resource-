#include<stdio.h>
#include<string.h>

struct employee{
    int code;
    float salary;
    char name[10];
};

int main(){
    struct employee e1, e2, e3;
    printf("Enter the value for code of e1: ");
    scanf("%d", &e1.code);
    printf("Enter the value for salary of e1: ");
    scanf("%f", &e1.salary);
    printf("Enter the value for name of e1: ");
    scanf("%s", e1.name);

    printf("Code is: %d \n", e1.code);
    printf("Salary is: %f \n", e1.salary);
    printf("Name is: %s \n", e1.name);
 
    return 0;
}