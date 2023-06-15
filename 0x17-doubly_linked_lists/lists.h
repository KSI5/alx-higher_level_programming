#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>
#include <stdlib.h>

/* Structures */

/**
 * struct dlistint_s - Doubly linked list node
 *
 * @n: Integer stored in the node
 * @prev: Pointer to the previous element of the list
 * @next: Pointer to the next element of the list
 */
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

/* Function Prototypes */

/* 0. Print doubly linked list */
size_t print_dlistint(const dlistint_t *h);

/* 1. Get the number of elements in a doubly linked list */
size_t dlistint_len(const dlistint_t *h);

/* 2. Add a new node at the beginning of a doubly linked list */
dlistint_t *add_dnodeint(dlistint_t **head, const int n);

/* 3. Add a new node at the end of a doubly linked list */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);

/* 4. Free a doubly linked list */
void free_dlistint(dlistint_t *head);

/* 5. Get the nth node of a doubly linked list */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index);

/* 6. Sum all the data (n) of a doubly linked list */
int sum_dlistint(dlistint_t *head);

/* 7. Insert a new node at a given position */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n);

/* 8. Delete the node at a given position */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index);

#endif /* LISTS_H */

