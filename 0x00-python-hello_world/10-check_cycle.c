#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: A singly linked list.
 *
 * Return: 1 if theres  a cycle,
 *		0 if theres no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
