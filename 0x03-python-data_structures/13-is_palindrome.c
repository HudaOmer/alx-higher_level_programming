#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: pointer to the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *p = NULL, i, count = 0, t = 0;
	listint_t *list = *head;

	if (!*head)
		return (1);
	while (list)
		list = list->next, t++;

	p = malloc(sizeof(int) + (t + 1));
	if (!p)
		return (0);
	list = *head;
	while (t)
	{
		*(p + count) = list->n;
		list = list->next;
		count++, t--;
	}
	for (i = 0; i < count / 2; i++)
	{
		if (p[i] != p[count - i - 1])
			return (0);
	}
	return (1);
}
