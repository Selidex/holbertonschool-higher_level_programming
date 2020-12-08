#include "lists.h"

/**
 *check_cycle - chekcs if a list has a cycle in it
 *@list: the list being checked
 *Return: 1 if cylce, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	int i = 0;

	if (list == NULL)
		return (0);

	while (current->next != NULL)
	{
		if (current->next == list || i == 1024)
			return (1);
		current = current->next;
		i++;
	}
	return (0);
}
