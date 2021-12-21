#include "lists.h"
#include <stdlib.h>

/**
* insert_node - Insert a number into a sorted linked list
*
* @head: The given sorted linked list
* @number: Number to fill inside
*
* Return: The pointer to the new element, NULL if it's doesn't work
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	if (*head == NULL || number < (*head)->n)
	{
		new = add_nodeint(head, number);
		return (new);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (current != NULL)
	{
		if (current->next == NULL || number < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		else
			current = current->next;
	}
	return (new);
}

/**
* add_nodeint - Add a new node a the begin of the list
*
* @head: Pointer to the start of the list.
* @n: Value to fill.
*
* Return: The new node.
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
