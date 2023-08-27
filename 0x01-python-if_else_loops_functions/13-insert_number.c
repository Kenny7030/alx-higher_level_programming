#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Description: Inserts a new node with the given number into a sorted
 * singly-linked list while maintaining the sorted order.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty or the new node should be the new head */
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the appropriate position for insertion */
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}

