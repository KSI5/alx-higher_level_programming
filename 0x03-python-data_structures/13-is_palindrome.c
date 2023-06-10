#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Double pointer to the head of the linked list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *mid_node = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		second_half = slow_ptr;
		reverse_listint(&second_half);
		while (second_half != NULL)
		{
			if ((*head)->n != second_half->n)
				palindrome = 0;

			*head = (*head)->next;
			second_half = second_half->next;
		}

		if (mid_node != NULL)
		{
			second_half = mid_node->next;
			reverse_listint(&second_half);
			mid_node->next = second_half;
		}
	}

	return (palindrome);
}

