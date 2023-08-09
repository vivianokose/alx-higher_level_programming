#include "lists.h"


typedef struct listint_s {
    int data;
    struct listint_s *next;
} listint_t;

/* Function to insert a number into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number) {
    /* Create a new node */
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;
    
    new_node->data = number;
    new_node->next = NULL;
    
    /* If the linked list is empty or the number is smaller than the head, insert at the beginning */
    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }
    
    /* Find the correct position to insert the new node */
    listint_t *current = *head;
    while (current->next != NULL && current->next->data < number) {
        current = current->next;
    }
    
    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;
    return new_node;
}
