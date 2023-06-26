#include<stdio.h>
#include<stdlib.h>

// * Value of oprator, 
struct myArray
{
    int total_size;
    int used_size;
    int *ptr;  // Here this is going to point my first element of my Array
};

void createArray(struct myArray * a, int tSize, int uSize){ // Here * a is struct type pointer 
    // (*a).total_size = tSize;
    // (*a).used_size = uSize;
    // (*a).ptr = (int *)malloc(tSize * sizeof(int));

    a->total_size = tSize;
    a->used_size = uSize; // Here the ptr is created in stack as pointer which store the address of memory which is created dynamically in heap 
    a->ptr = (int *)malloc(tSize * sizeof(int));  // Here this is going to create memory in heap and *ptr going to return point the first element of memory 
}

void show(struct myArray *a){
    for (int i = 0; i < a->used_size; i++)
    {
        printf("%d\n", (a->ptr)[i]);
    }
}

void setVal(struct myArray *a){
    int n;
    for (int i = 0; i < a->used_size; i++)
    {
        printf("Enter element %d", i);
        scanf("%d", &n);
        (a->ptr)[i] = n;
    }
    
}

int main(){
    struct myArray marks;
    createArray(&marks, 10, 7);
    printf("We are running setVal now\n");
    setVal(&marks);

    printf("We are running show now\n");
    show(&marks);

    return 0;
}