#include <stddef.h>
#include "lists.h"


listint_t *rvs_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * rvs_listint - Reverse list.
 * @head: A pointer
 * Return: pointer
 *
 */

listint_t *rvs_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prv = NULL;

	while (node)
	{
		next = node->next;
		node->next = prv;
		prv = node;
		node = next;
	}
	*head = prv;
	return (*head);
}




/**
 * is_palindrome - Checks if is a palindrome.
 * @head: A pointer
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 *
 */


int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rvs, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rvs = rvs_listint(&tmp);
	mid = rvs;

	tmp = *head;
	while (rvs)
	{
		if (tmp->n != rvs->n)
			return (0);
		tmp = tmp->next;
		rvs = rvs->next;
	}
	rvs_listint(&mid);
	return (1);
}
