#include "lists.h"

/**
 *insert_node - inserts node into a sorted list
 *@head: the list being instered
 *@number: the number being inserted
 *Return: address of new node, or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->next = NULL;
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
	while (current->next != NULL)
	{
		if (number < current->next->n)
			break;
		current = current->next;
	}

	new->next = current->next;
	current->next = new;
	return (new);
}
