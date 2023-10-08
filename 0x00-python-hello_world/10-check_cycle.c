#include "list.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - detects if there is a cycle in a linked list
 * list: list to detect
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *second = list;
	listint_t *first = list;

	while (first && first->next)
	{
		second = second->next; /*moves one node at a time*/
		first = first->next->next; /*moves two nodes at a time*/
		if (first == second)
			return (1);
	}
	return (0);
}
