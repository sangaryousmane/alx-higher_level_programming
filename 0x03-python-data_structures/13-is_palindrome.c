#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
	listint_t *prev = NULL, *current = *head, *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (; fast; fast = fast->next->next)
	{
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	for (; current != dup; current = next)
	{
		next = current->next;
		current->next = prev;
		prev = current;
	}

	if (fast)
		dup = dup->next;
	for (; dup && temp; dup = dup->next, temp = temp->next)
	{
		if (temp->n != dup->n)
			return (0);
	}
	return (!dup);
}
