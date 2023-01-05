#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 *
 * Return: 0 if cycle, 1 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
