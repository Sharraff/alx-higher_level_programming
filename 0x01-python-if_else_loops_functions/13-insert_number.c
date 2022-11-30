#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insertd node in ordered list
 * @head: head of list
 * @number: number to put in
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;

	temp = *head;
	new malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if ((*head) == NULL)
	{

		*head = new;
		return (new);
	}
	else if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (tmp->next != NULL)
		{
			if (tmp->next->n >= number)
			{
				new->next = tmp->next;
				tmp->next = new;
				return (new);
			}
			tmp = tmp->next;
		}
		new->next = NULL;
		tmp->next = new;
		return (new);
	}
	return (NULL);
}
