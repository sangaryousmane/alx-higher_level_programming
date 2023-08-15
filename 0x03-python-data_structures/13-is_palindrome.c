#include "lists.h"

/**
 * is_palindrome - checks for palindrome in a linked list
 * @head: head of the structure that mimics a linked list
 * Return: 0 if not palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp = slow->next, *next;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	
	while (temp != NULL)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	listint_t *p1 = *head, *p2 = prev;
	
	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);
}
