#include "lists.h"

int checktest(listint_t *test, int address)
{
	listint_t *current = test;

	while (current->next != NULL)
	{
		if (current->n == address)
			return (1);
		else
			current = current->next;
	}
	return (0);
}





int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *test;


	while (current->next != NULL)
	{
		if (checktest(test, &(current->next)) != 0)
		{
			free_listint(test);
			return (1);
		}
		else
			add_nodeint(&test, &(current->next));
		current = current->next;
	}
	free_listint(test);
	return (0);
}
