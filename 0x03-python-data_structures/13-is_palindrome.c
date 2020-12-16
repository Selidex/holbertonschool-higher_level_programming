#include "lists.h"

/**
 *list_len - produces the length of a linked list
 *@head: the list
 *Return: the lenght of the list
 */

int list_len(listint_t *head)
{
	listint_t *current = head;
	int i = 0;

	while (current != NULL)
	{
		i++;
		current = current->next;
	}
	return (i);
}

/**
 *is_palindrome - checks if a given sll is a palindrome
 *@head: the list being checked
 *Return: 0 if pal, 1 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i = 0, *arr, ll;

	if (current == NULL)
		return (1);
	ll = list_len(current);
	arr = calloc(ll, sizeof(int));
	if (arr == NULL)
		return (0);

	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0; i < (ll / 2); i++)
	{
		if (arr[i] != arr[ll - i - 1])
			return (0);
	}
	return (1);
}
