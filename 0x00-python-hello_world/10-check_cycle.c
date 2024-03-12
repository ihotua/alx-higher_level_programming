#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list contains a cycle
 * 
 * @list: pointer to the list
 * 
 * Return: 0 if there's no cycle, 1 if there's a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ihotu; 
	listint_t *nathan;

	if (list == NULL || list->next == NULL)
		return (0);

	ihotu = list->next;
	nathan = list->next->next;

	while (ihotu && nathan && nathan->next)
	{
		if (ihotu == nathan)
			return (1);

		ihotu = ihotu->next;
		nathan = nathan->next->next;
	}

	return (0);
}
