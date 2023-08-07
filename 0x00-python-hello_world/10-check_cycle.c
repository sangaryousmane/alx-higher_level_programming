#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for cycle in a singly linked list
 * @list: the singly linked list
 * Return: 1 if there is cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	int steps = 0, strength = 1;
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	turtle = list;
	hare = list->next;

	while (hare != NULL)
	{
		if (turtle == hare)
		{
			return (1);
		}
		if (steps == strength)
		{
			steps = 0;
			strength *= 2;
			turtle = hare;
		}
		hare = hare->next;
		steps++;
	}
	return (0);
}
