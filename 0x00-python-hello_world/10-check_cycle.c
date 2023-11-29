#include "lists.h"

/**
 * check_cycle - checks if there is a loop in a list
 * @list: the pointer to the start of the list
 * Return: 1 if there is cycle
 *          Otherwise: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (1)
	{
		if (fast == NULL)
			return (0);

		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}
}
