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

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (h && h->next && h->next->n < number)
	{
		h = h->next;
	}

	new->next = h->next;
	h->next = new;

	return (new);
}
