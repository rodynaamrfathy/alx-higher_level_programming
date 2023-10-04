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
	listint_t *check = list;

	check = check->next;
	while (check != list)
	{
		check = check->next;
		if (check == NULL)
			return (0);
	}
	return (1);
}
