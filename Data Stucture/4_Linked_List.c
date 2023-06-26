#include <stdio.h>
#include <stdlib.h>

struct Node     // This is struct node which stores the data and a pointer
{
    int data;
    struct Node *next; // Ye struct node type ka pointer hai ** This is a pointer which point the another struct node data 
};

void linkedListTraversal(struct Node *ptr) // Here we need struct node * type of pointer which point the head struct node. Here head is struct node pointer
{
    while (ptr != NULL)
    {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;   // This will point the next element of struct node
    }
}

int main()
{
    struct Node *head = (struct Node *)malloc(sizeof(struct Node)); // Here this head is known as the struct pointer 
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    // Allocate memory for nodes in the linked list in Heap
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    fourth = (struct Node *)malloc(sizeof(struct Node));

    // Link first and second nodes
    head->data = 7;   // Here -> this is known as arrow oprator and this is use for set the value  
    head->next = second;

    // Link second and third nodes
    second->data = 11;
    second->next = third;

    // Link third and fourth nodes
    third->data = 41;
    third->next = fourth;

    // Terminate the list at the third node
    fourth->data = 66;
    fourth->next = NULL;

    linkedListTraversal(head);  // Here head is a pointer struct node * type ka
    return 0;
}