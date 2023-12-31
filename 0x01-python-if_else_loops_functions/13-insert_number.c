#include <stdbool.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the start of the list.
 * @number: the value of the new block to insert.
 *
 * Return: the address to the new block.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **current = head,
			  **prev = head,
			  *new_block;

	if (*head)
		while (true)
		{
			if ((*current)->n > number)
				break;
			if ((*current)->next)
			{
				prev = current;
				current = &((*current)->next);
			}
		}

	new_block = malloc(sizeof(listint_t));
	if (!new_block)
		return (NULL);

	new_block->n = number;
	if (*head)
	{
		new_block->next = *current;
		(*prev)->next = new_block;
	}
	else
	{
		new_block->next = NULL;
		(*head) = new_block;
	}

	return (new_block);
}
