#include "list.h"

/**
 * insert_node- Inserts a number into a singly-linked sorted list.
 * @head: Head of a list.
 * @number: The number to insert.
 * Return: 0 if it fails or address to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *head;
	listint_t *new_node = malloc(sizeof(listint_t));
	
	if (new_node == NULL)
		return (NULL);
	new_node -> = number;
	
	if (node == NULL || node -> >= number)
	{
		new_node -> next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node -> next && node -> next -> n < number)
		node = node -> next;

	new_node -> next = node -> next;
	node -> next = new_node;

	return (new_node);
}
