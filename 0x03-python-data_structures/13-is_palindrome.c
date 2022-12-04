#include "lists.h"

/**
 * reverse_listint - reverses a singly linked list.
 * @head: pointer to the first node in the list.
 *
 * Return: pointer to the head of the new list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *temp = *head, *mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (fast->next == NULL) /* odd list */
		{
			mid = slow->next->next;
		break;
		}
		if (fast == NULL) /* even list */
		{
			mid = slow->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&mid);

	while (mid && temp)
	{
		if (temp->n != mid->n)
			return (0);
		mid = mid->next;
		temp = temp->next;
	}
	if (!mid)
		return (1);

	return (0);
}
