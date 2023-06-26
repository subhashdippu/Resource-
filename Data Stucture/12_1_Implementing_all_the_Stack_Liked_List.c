#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};
struct Node *top = NULL; // This is going to become global value
void linkedListTraversal(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;
    }
}

int Empty(struct Node *top)
{
    if (top == NULL)
    {
        return 1;
    }
    return 0;
}

int Full(struct Node *top)
{
    struct Node *p = (struct Node *)malloc(sizeof(struct Node));
    if (p == NULL)
    {
        return 1;
    }
    return 0;
}

struct Node *push(struct Node *top, int val)
{
    if (Full(top))
    {
        printf("Stack is OverFlow");
    }
    else
    {
        struct Node *q = (struct Node *)malloc(sizeof(struct Node));
        q->data = val;
        q->next = top;
        top = q;
        return top;
    }
}

int pop(struct Node *tp)
{
    if (Empty(tp))
    {
        printf("Stack is Underflow");
    }
    else
    {
        struct Node *n = top;
        top = top->next;
        int x = n->data;
        free(n);
        return x;
    }
}
int main()
{

    top = push(top, 45); // This will update the top
    top = push(top, 7);  // Here this function is going to return new top
    top = push(top, 8);

    linkedListTraversal(top);
    int element = pop(top); // This method is use for printing the returning value // Here this top will going to change only in fuction. Iska main fuction se koi matlab nhi 
    printf("Poped element %d\n", element);
    linkedListTraversal(top);

    // linkedListTraversal(top);
    // if(Empty(top)){
    //     printf("The stack is empty");
    // }
    // else{
    //     printf("The stack is not empty");
    // }

    return 0;
}
