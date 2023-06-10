#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *temp;

	/* Find the middle of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	/* Handle odd-length palindrome */
	if (fast != NULL)
		slow = slow->next;

	/* Compare values of first half and reversed second half */
	while (slow != NULL)
	{
		if (current->n != slow->n)
			return (0);
		current = current->next;
		slow = slow->next;
	}

	return (1);
}

