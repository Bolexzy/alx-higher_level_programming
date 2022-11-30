#include "lists.h"

/**
 * insert_node - inserts a new number into a sorted singly-linked list.
 *
 * @head: head of the linked list.
 * @number: The number to insert
 *
 * Return: the address of the new node,
 *		or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h = *head;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
	}

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}

	new->next = h;
	prev->next = new;

	return (new);
}
