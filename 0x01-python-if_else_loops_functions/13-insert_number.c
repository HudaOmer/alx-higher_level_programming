#include "lists.h"

/**
 * insert_node - insert node in a sotred array
 * @head: of the list
 * @number: to be inserted
 * best case is to have no element
 * at least one element
 * Return: pointer to the inserted node, Null on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head, *hold;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	if (!*head)
  {
    new->next = NULL;
    *head = new;
    return (new);
  }

	new->n = number;
  while (temp)
  {
    if (number < temp->n)
      break;
    hold = temp;
    temp = temp->next;
  }

  newl->next = temp;

  if (temp == *head)
    *head = new;
  else
  	hold->next = new;

  return (new);
}
