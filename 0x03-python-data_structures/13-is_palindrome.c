#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, 
        *slow = *head,
        *temp_head = *head;
    int length_of_list = 0,
    paired_items_counter = 0;

    while (fast)
    {
        fast = fast->next->next;
        slow = slow->next;

        length_of_list++;
    }

    while (slow)
    {
        if (slow->n == temp_head->n)
            paired_items_counter++;
        printf("He %d, %d\n", slow->n, temp_head->n);
        slow = slow->next;
        temp_head = temp_head->next;
    }

    return (paired_items_counter == length_of_list ? 1 : 0);
}
