#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - this is a function that checks if the linked list is a cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && slow != NULL && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast ==  slow)
			return (1);
	}
	return (0);
}
