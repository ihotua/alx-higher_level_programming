#include "lists.h"

/**
 * reverse_listint - Reverses a singly linked list.
 * @head: A pointer to the head of the list.
 *
 * Return: A pointer to the new head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = *head, *second_half = NULL;
    listint_t *midnode = NULL, *tmp = *head;
    int res = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        midnode = slow;
        slow = slow->next;
    }

    second_half = reverse_listint(&slow);

    while (second_half != NULL)
    {
        if (tmp->n != second_half->n)
        {
            res = 0;
            break;
        }
        tmp = tmp->next;
        second_half = second_half->next;
    }

    reverse_listint(&slow);

    if (midnode != NULL)
    {
        prev_slow->next = midnode;
        midnode->next = slow;
    }
    else
        prev_slow->next = slow;

    return res;
}
