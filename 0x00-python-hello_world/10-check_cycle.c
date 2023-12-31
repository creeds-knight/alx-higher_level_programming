#include "lists.h"
/**
 * check_cycle - A function that checks if a singly list has a cycle in it
 * @list: The list to be checked
 * Return: 0 if there is no cycle and 1 if there is one
 */
int check_cycle(listint_t *list)
{
	listint_t *checked_node = list;
	listint_t *tmp = list;

	while (tmp !=NULL && tmp->next != NULL)
	{
		tmp = tmp->next->next;
		checked_node = checked_node->next;
		if (tmp == checked_node)
			return (1);
	}
	return (0);
}
