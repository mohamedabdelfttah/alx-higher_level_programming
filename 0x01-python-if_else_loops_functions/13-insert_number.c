#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the first node
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current = *head;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
current->n = number;

new_node->n = number;
new_node->next = NULL;

if (current == NULL || current->n >= number)
{
new_node->next = current;
*head = new_node;
return (new_node);
}

while (current && current->next && current->next->n < number)
current = current->next;

new_node->next = current->next;
current->next = new_node;


return (new_node);
}
