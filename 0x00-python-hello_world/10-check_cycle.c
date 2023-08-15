#include "lists.h"

/**
 * check_cycle - Function that checks if a linked list contains a cycle
 * @list: The linked list to check for a cycle
 * Return: 1 if cycle exists, 0 if no cycle is found
 */

int check_cycle(listint_t *list)
{
    listint_t *fast = list;
    listint_t *slow = list;

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

