#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *pre;
    struct Node *next;
};

void display(struct Node *ptr){
    while (ptr != NULL)
    {   
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;   // This will point the next element of struct node
    }

}
int main(){
    struct Node *n1 = (struct Node *) malloc(sizeof(struct Node));
    struct Node *n2 = (struct Node *) malloc(sizeof(struct Node));
    struct Node *n3 = (struct Node *) malloc(sizeof(struct Node));
    struct Node *n4 = (struct Node *) malloc(sizeof(struct Node));

    n1->next = n2;
    n1->pre = NULL;
    n1->data = 14;

    n2->next = n3;
    n2->pre = n1;
    n2->data = 11;

    n3->next = n4;
    n3->pre = n2;
    n3->data = 140;

    n4->next = NULL;
    n4->pre = n3;
    n4->data = 17;

    display(n1);
    return 0;
}